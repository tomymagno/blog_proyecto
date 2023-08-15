# blog/urls.py
from django.urls import path
from blog.views import create_article, edit_article, delete_article, article_detail

urlpatterns = [
    path('create/', create_article, name='create_article'),
    path('edit/<int:article_id>/', edit_article, name='edit_article'),
    path('delete/<int:article_id>/', delete_article, name='delete_article'),
    path('<int:article_id>/', article_detail, name='article_detail'),
    
]
