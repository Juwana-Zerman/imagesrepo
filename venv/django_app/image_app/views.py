from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from .models import Post
from django.views.generic import ListView

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

class imagePageView(ListView):
    model = Post
    template_name = 'index.html'