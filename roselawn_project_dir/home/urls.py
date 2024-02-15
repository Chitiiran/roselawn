from django.urls import path
from .views import *
from .views import PortfolioView
urlpatterns = [
    path('', landing_page),
    # path('portfolio/', portfolio),
    # path('contact/', contact),
    # path('test/', testtest),
    path('serial/', PortfolioView.as_view(), name='namenamename')
]