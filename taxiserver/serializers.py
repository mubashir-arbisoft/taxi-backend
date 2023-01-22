from rest_framework import serializers
from taxiserver.models import User, Car, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'is_driver')


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name', 'price', 'seats', 'large_suitcases', 'carry_on_bags', 'id')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('user', 'car', 'date', 'id')

