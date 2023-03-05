from django.contrib import admin
from .models import User, Car, Booking, CarType

admin.site.register(User)
admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(Booking)
# Register your models here.
