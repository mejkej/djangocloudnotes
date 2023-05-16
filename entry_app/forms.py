from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class CustomSignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.PasswordInput, max_length=20, min_length=5)