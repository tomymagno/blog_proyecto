# perfiles/views.py
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .models import Perfil

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Crear el perfil asociado al usuario recién creado
            perfil = Perfil.objects.create(user=user, nombre=form.cleaned_data['nombre'], apellido=form.cleaned_data['apellido'])

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'perfiles/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'perfiles/login.html', {'form': form})

def profile(request):
    user_profile = request.user.perfil
    return render(request, 'perfiles/profile.html', {'user_profile': user_profile})

def logout_view(request):
    logout(request)
    return redirect('home')