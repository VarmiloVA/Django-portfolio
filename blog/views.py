from django.shortcuts import render
from .models import Topic, Content

def index(request):
    """Blog main page"""
    return render(request, 'blog/index.html')

def topic(request):
    """All topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'#ver para que sirve en el libro'}
    return render(request, 'blog/topic.html', context)

def about_me(request):
    """Who's writting this?"""
    return render(request, 'blog/about_me.html')