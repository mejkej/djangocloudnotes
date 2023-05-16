from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
]
