from django.shortcuts import render
from .models import Post

def index(request):
    """Main Blog page"""
    return render(request, 'blog/index.html')

def posts(request):
    """Posts page"""
    posts = Post.objects.order_by('date_added')
    context = {'posts': 'content'}
    return render(request, 'blog/posts.html')