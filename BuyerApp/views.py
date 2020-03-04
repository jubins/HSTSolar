from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from SellerApp.models import SellerListings
import numpy as np


def get_distance(lat, lng):
    """
    Formula to compute distance between two lat/lng pairs in miles
    :param lat: Float Tuple, Latitude1, Latitude2
    :param lng: Float Tuple, Longitude1, Longitutde2
    :return: Float, Distance in miles.
    """
    if not lat or not lng:
        return None
    lat1, lat2 = lat
    lon1, lon2 = lng
    if not lat1 or not lat2 or not lon1 or not lon2:
        return None
    lat1, lat2, lon1, lon2 = float(lat1), float(lat2), float(lon1), float(lon2)
    dist = np.rad2deg(np.arccos(np.sin(np.deg2rad(lat1)) * np.sin(np.deg2rad(lat2)) +
                                np.cos(np.deg2rad(lat1)) * np.cos(np.deg2rad(lat2)) *
                                np.cos(np.deg2rad(lon1 - lon2)))) * 60 * 1.1515 * 1.60934
    return dist


def sort_by_price(content):
    data = list()
    prices = dict()
    for idx, d in enumerate(content):
        if d['price'] in prices:
            prices[d['price']].append(idx)
        else:
            prices[d['price']] = [idx]
    for p in sorted(prices.keys()):
        for idx in prices[p]:
            data.append(content[idx])
    return data


def get_results_within_criteria(within, amount, lat1, lng1, filters=True):
    content = list()
    seller_listings = SellerListings.objects.all()
    if not filters:
        for field in seller_listings:
            lat2, lng2 = field.latitude, field.longitude
            if not lat1 and lat2:
                lat1 = 40
                lng1 = -74
            dist = get_distance((lat1, lat2), (lng1, lng2))
            data = {'id': field.id, 'name': field.name, 'longitude': '{}'.format(field.longitude),
                    'latitude': '{}'.format(field.latitude), 'amount': field.amount, 'price': field.price,
                    'distance': '{:.5f}'.format(dist)}
            content.append(data)
        return sort_by_price(content)
    else:
        for field in seller_listings:
            lat2, lng2 = field.latitude, field.longitude
            dist = get_distance((lat1, lat2), (lng1, lng2))
            if dist is None or within is None:
                continue
            if 0 <= dist <= within and 0 <= field.amount <= amount:
                data = {'id': field.id, 'name': field.name, 'longitude': '{}'.format(field.longitude),
                        'latitude': '{}'.format(field.latitude), 'amount': field.amount, 'price': field.price,
                        'distance': '{:.5f}'.format(dist)}
                content.append(data)
        return sort_by_price(content)


def view_listing(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    context = search_results(request)
    if latitude and longitude:
        return JsonResponse(context)
    else:
        return render(request, 'BuyerApp/ViewListings.html', context)


def search_results(request):
    within = float(request.GET.get('within')) if request.GET.get('within') else None
    amount = float(request.GET.get('amount')) if request.GET.get('amount') else None
    lat1, lng1 = request.GET.get('latitude'), request.GET.get('longitude')
    context = get_results_within_criteria(within, amount, lat1, lng1)
    if not context:
        context = get_results_within_criteria(within, amount, lat1, lng1, filters=False)
    return {'listings': context}
