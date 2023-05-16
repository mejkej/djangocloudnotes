from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, SignInForm
from django.core.exceptions import ValidationError


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_app/signin.html')
    else:
        form = SignUpForm()

    return render(request, 'entry_app/signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')  # Redirect to main_app or another page after successful login
            else:
                raise ValidationError('Username or password incorrect.')
    else:
        form = SignInForm()

    return render(request, 'entry_app/signin.html', {'form': form})

