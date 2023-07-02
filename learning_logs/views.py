from django.shortcuts import render
from .models import Topic

def index(request):
    """Index page for learning_logs"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Page in which all topics will be shown"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)