"""URL patterns for learning_logs"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Topics page
    path('topics/', views.topics, name='topics'),
    #Topic entries
    path('topic/<int:topic_id>/', views.topic , name='topic')
]