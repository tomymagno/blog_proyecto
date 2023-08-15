# perfiles/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField()

class LoginForm(AuthenticationForm):
    pass
