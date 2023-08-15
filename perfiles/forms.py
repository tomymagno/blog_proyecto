from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Perfil

class SignupForm(UserCreationForm):
    email = forms.EmailField()

class LoginForm(AuthenticationForm):
    pass

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'apellido', 'avatar']