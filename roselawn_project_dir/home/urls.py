from django.urls import path
from .views import *

urlpatterns = [
    path('room/', RoomView.as_view(), name='RoomView'),
    path('create-room/', CreateRoomView.as_view(), name="CreateRoomView")
]