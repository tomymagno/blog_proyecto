# perfiles/urls.py
from django.urls import path
from perfiles.views import signup, login_view, profile, logout_view 

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    # Agrega más URLs según las necesidades
]
