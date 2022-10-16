"""Defines URLs patterns for blog"""

from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    #Main blog page
    path('', views.index, name='index'),
]