"""Defines URLs patterns for blog"""

from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    #Main blog page
    path('index/', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
]