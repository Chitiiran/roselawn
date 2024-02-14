from django.shortcuts import render
from django.conf import settings

def landing_page(request):
    return render(request, 'home/landing_page.html')

def portfolio(request):
    context = {'MEDIA_URL': settings.MEDIA_URL}
    return render(request, 'home/portfolio.html', context)
