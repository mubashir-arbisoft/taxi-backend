from rest_framework import serializers
from taxiserver.models import User, Car, Booking, CarType

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'is_driver')


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ('name', 'price', 'seats', 'large_suitcases', 'carry_on_bags', 'id')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('user', 'car_type', 'time', 'id', 'price', 'num_of_passengers',
        'booking_for_another',
        'passenger_firstname',
        'passenger_lastname',
        'passenger_phone',
        'flight_no',
        'name_board',
        'additional_req',
        'start_geo_lt',
        'start_geo_ln',
        'start_addr',
        'end_geo_lt',
        'end_geo_ln',
        'end_addr',
        'firstname',
        'lastname',
        'phone')

