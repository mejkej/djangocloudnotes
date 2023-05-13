from django.urls import path
from . import views


urlpatterns = [
    path('signin/', signin_view, name='signin'),
    path('signup/', signup_view, name='signup'),
]