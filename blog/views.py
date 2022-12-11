from django.shortcuts import render
from .models import Topic

def index(request):
    """Blog main page"""
    return render(request, 'blog/index.html')

def topics(request):
    """All topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blog/topics.html', context)

def topic(request, topic_id):
    """Shows individually a topic"""                          
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')     
    context = {'topic': topic, 'entries': entries}
    return render(request, 'blog/topic.html', context)

def about_me(request):
    """About me page"""
    return render(request, 'blog/about_me.html')