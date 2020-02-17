from django.shortcuts import render


def homepage(request):
    context = dict()
    return render(request, 'Dashboard/Homepage.html', context)

