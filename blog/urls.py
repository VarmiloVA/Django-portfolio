"""URLs patterns for blog app"""
from django.urls import path

from . import views
app_name = "blog"
urlpatterns = [
    #index
    path('', views.index, name='index'),
    #topics
    path('topics/', views.topics, name='topics'),
    #individual topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    #about me
    path('about_me/', views.about_me, name='about_me')
] 