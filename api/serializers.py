from datetime import datetime
from rest_framework import serializers
from api.models import (
    User,
    Travel,
    Picture,
    TravelLog,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TravelSerializer(serializers.ModelSerializer):
    departure_datetime = serializers.SerializerMethodField()
    boarding_datetime = serializers.SerializerMethodField()

    def get_departure_datetime(self, obj):
        date_ori = obj['departure_datetime']
        if date_ori:
            date_str = date_ori.strftime('%d/%m/%Y %H:%M')
            return date_str.upper()
        return date_ori

    def get_boarding_datetime(self, obj):
        date_ori = obj['boarding_datetime']
        if date_ori:
            date_str = date_ori.strftime('%d/%m/%Y %H:%M')
            return date_str.upper()
        return date_ori
    
    class Meta:
        model = Travel
        fields = '__all__'

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'

class TravelLogSerializer(serializers.ModelSerializer):
    travel_departure_datetime = serializers.SerializerMethodField()
    travel_boarding_datetime = serializers.SerializerMethodField()

    def get_travel_departure_datetime(self, obj):
        date_ori = obj['travel_departure_datetime']
        if date_ori:
            date_str = date_ori.strftime('%d/%m/%Y %H:%M')
            return date_str.upper()
        return date_ori

    def get_travel_boarding_datetime(self, obj):
        date_ori = obj['travel_boarding_datetime']
        if date_ori:
            date_str = date_ori.strftime('%d/%m/%Y %H:%M')
            return date_str.upper()
        return date_ori
    
    class Meta:
        model = TravelLog
        exclude = ('user',)
