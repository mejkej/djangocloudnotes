from django.shortcuts import render, redirect

# Create your views here.
def signin_view(request):
    return render (request, entry_app/signin.html)