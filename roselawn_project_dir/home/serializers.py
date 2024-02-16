from rest_framework import serializers
from .models import PortfolioItem, Room

class PortfolioItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioItem
        fields = ('name','title', 'price', 'description')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id',
                  'code',
                  'guest_can_pause',
                  'votes_to_skip',
                  'created_at',
                 )

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause',
                  'votes_to_skip',
                 )
