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

def topic(request, topic_id):
    """Shows the content created about a topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic, 
        'entries': entries,
        }
    return render(request, 'learning_logs/topic.html', context)