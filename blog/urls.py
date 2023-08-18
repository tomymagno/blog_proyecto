# blog/urls.py
from django.urls import path
from blog.views import about, article_list, article_detail, create_article, edit_article, delete_article

urlpatterns = [
    path('about/', about, name='about'),
    path('article_list/', article_list, name='article_list'),
    path('article_detail/<int:article_id>/', article_detail, name='article_detail'),
    path('create_article/', create_article, name='create_article'),
    path('edit_article/<int:article_id>/', edit_article, name='edit_article'),
    path('delete_article/<int:article_id>/', delete_article, name='delete_article'),
]