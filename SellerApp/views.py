from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
from .models import SellerListings


def insert_records(data):
    headers = {'project_name', 'longitude', 'latitude', 'amount', 'price'}
    data = {h: data.get(h) for h in headers}
    sl = SellerListings(name=data['project_name'], longitude=data['longitude'], latitude=data['latitude'],
                        amount=data['amount'], price=data['price'])
    sl.save()


def delete_records(data):
    document_id = data['document_id'].split('_')[-1]
    SellerListings.objects.filter(id=document_id).delete()


def create_listing(request):
    if request.GET.get('create_listing') == 'true':
        insert_records(request.GET)
    if request.GET.get('delete_listing') == 'true':
        delete_records(request.GET)

    seller_listings = SellerListings.objects.all()
    content = list()
    for field in seller_listings:
        data = {'id': field.id, 'name': field.name, 'longitude': field.longitude,
                'latitude': field.latitude, 'amount': field.amount, 'price': field.price}
        content.append(data)
    context = {'listings': content}
    return render(request, 'SellerApp/CreateListings.html', context)

