from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

from django.shortcuts import render

 
app_name = 'taxiserver'

urlpatterns = [
    path('api/register/', views.register_user, name="register"),
    path('api/login/', views.login_request, name="login"),
    path('api/logout/', views.logout_request, name="logout"),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)