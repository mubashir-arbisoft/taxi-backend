from django.shortcuts import render
import datetime
import json
import pytz

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

from taxiserver.models import User

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
        user = User.objects.create_user(body['name'], body['email'], body['password'])
        user.save()
        return JsonResponse({'success': "Registered as normal User."})
    except Exception as e:
        print(e)
        return JsonResponse({'error': "Username or Email already exists"})


@ensure_csrf_cookie
def login_request(request):
    if request.method == "POST":
        body = json.loads(request.body)
        user = authenticate(username=body['email'], password=body['password'])
        if user is not None:
            login(request, user)
            return JsonResponse({'Success': 'Logged In'})
        else:
            return JsonResponse({'error': "Invalid email or password."})       


def logout_request(request):
    logout(request)
    return JsonResponse({'Success': 'Logged Out'})
