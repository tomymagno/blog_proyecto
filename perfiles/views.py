# perfiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, LoginForm, PerfilForm
from .models import Perfil

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Crear el perfil asociado al usuario recién creado
            perfil = Perfil.objects.create(
                user=user,
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido']
            )

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
    try:
        user_profile = request.user.perfil
    except Perfil.DoesNotExist:
        # Si el perfil no existe para el usuario, redirige a la página de creación o edición de perfil (tendríamos que crearla)
        return redirect('create_profile')
    return render(request, 'perfiles/profile.html', {'user_profile': user_profile})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def edit_profile(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
    if form.is_valid():
        form.save()
        return redirect('profile')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'perfiles/edit_profile.html', {'form': form})

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.user = request.user
            perfil.save()
            return redirect('profile')
    else:
        form = PerfilForm()

    return render(request, 'perfiles/create_profile.html', {'form': form})

