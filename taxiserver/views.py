from django.shortcuts import render
import datetime
import json
import pytz
import stripe

from asgiref.sync import AsyncToSync

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator, PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMultiAlternatives
from django.db.models import Sum, Count, Avg
from django.db.models.functions import TruncDate
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from django.template import Context
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, permissions, filters
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from taxiserver.models import User, Car, Booking, CarType
from taxiserver.serializers import UserSerializer,  BookingSerializer, CarTypeSerializer



stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://localhost:3000'

def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '?success=true',
            cancel_url=YOUR_DOMAIN + '?canceled=true',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


def stripe_payment(request):
    if request.method == 'POST':
        # Get the payment token ID submitted by the form
        stripe.api_key = 'sk_test_51M8sO4KV3JdLpOOyNi8FGx9K4mI9Ah5NtCF9MiwKwLXwRwX1errFRVEVYDQNTsyIEJkNDrO5qIXxSMRJoVdKavgG00vduQ6wIP'
        booking = Booking.objects.get(id=json.loads(request.body)['id'])
        #intent = stripe.PaymentIntent.create(
        #amount=int(booking.price * 100),
        #currency='usd',
        #)
        intent = stripe.PaymentIntent.create(
        amount=50,
        currency='usd',
        )
        client_secret = intent.client_secret
        return JsonResponse({'clientSecret': client_secret})



class CarTypeList(generics.ListCreateAPIView):
    serializer_class = CarTypeSerializer
    queryset = CarType.objects.all()

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    

class BookingList(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

# Create your views here.
class RegisterDriver(APIView):
    permission_classes = []
    def post(self, request):
        body = request.data
        try:
            user = User.objects.create_user(body['username'], body['email'])
            user.is_staff = True
            user.save()
            return JsonResponse({'success': "Driver Added."})
        except:
            return JsonResponse({'error': "Username or Email already exists"})

@api_view(['POST'])
def register_user(request):
    body = json.loads(request.body)
    try:
        user = User.objects.create_user(body['email'], body['password'], body['name'])
        user.save()
        return JsonResponse({'success': "Registered as normal User."})
    except Exception as e:
        print(e)
        return JsonResponse({'error': "Username or Email already exists"})

@ensure_csrf_cookie
def login_request(request):
    if request.method == "POST":
        body = json.loads(request.body)
        user = authenticate(request, email=body['email'], password=body['password'])
        if user is not None:
            login(request, user)
    
            user_serializer = UserSerializer(user).data
            return JsonResponse({'user': user_serializer})
        else:
            return JsonResponse({'error': "Invalid email or password."})       

def logout_request(request):
    logout(request)
    return JsonResponse({'success': 'Logged Out'})
