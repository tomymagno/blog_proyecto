# perfiles/urls.py
from django.urls import path
from perfiles.views import signup, login_view, profile, logout_view, edit_profile

app_name = 'perfiles'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile')
    # Agrega más URLs según las necesidades
]
