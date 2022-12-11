"""URLs patterns for portfolio app"""
from django.urls import path
from . import views

app_name = "portfolio"
urlpatterns = [
    #index (the portfolio itself)
    path('', views.index, name="index")
]