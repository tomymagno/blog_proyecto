# perfiles/urls.py
from django.urls import path
from perfiles.views import signup, login_view, profile 

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    # Agrega más URLs según las necesidades
]
