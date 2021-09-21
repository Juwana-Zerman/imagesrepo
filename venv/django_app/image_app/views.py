from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    """Renders the home page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )