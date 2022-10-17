from django.shortcuts import render

def index(request):
    """Main Blog page"""
    return render(request, 'blog/index.html')