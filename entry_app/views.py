from django.shortcuts import render, redirect
from .forms import UserCreationForm

# Create your views here.
def signin_view(request):
    return render(request, 'signin')

def signup_view(request):
    return render(request, 'signup')