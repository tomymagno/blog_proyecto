from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Perfil

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    nombre = forms.CharField(max_length=30)  # Campo para el nombre
    apellido = forms.CharField(max_length=30)   # Campo para el apellido

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                    'password2', 'nombre', 'apellido']

class LoginForm(AuthenticationForm):
    pass

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'apellido', 'avatar']