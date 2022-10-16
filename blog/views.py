from django.shortcuts import render

def index(request):
    """Main Blog page"""
    return request(request, 'learning_logs/index.html')