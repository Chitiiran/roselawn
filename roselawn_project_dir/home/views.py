from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from rest_framework import generics
from .serializers import PortfolioItemSerializer
from .models import PortfolioItem

def landing_page(request):
    return render(request, 'home/landing_page.html')

def portfolio(request):
    context = {'MEDIA_URL': settings.MEDIA_URL}
    return render(request, 'home/portfolio.html', context)

def contact(request):
    return render(request, 'home/contact.html')

def testtest(request):
    return HttpResponse("Test test is working")

class PortfolioView(generics.ListCreateAPIView):
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioItemSerializer