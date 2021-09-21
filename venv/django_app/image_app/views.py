from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from .models import Post
from django.views.generic import ListView, CreateView, DeleteView

from django.urls import reverse_lazy
from .forms import imagePostForm, imageDeleteForm

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

class createPostView(CreateView):
    model = Post
    template_name = 'add_image.html'
    form_class = imagePostForm
    success_url = reverse_lazy('home')

class deletePostView(DeleteView):
    model = Post
    template_name = 'delete_image.html'
    success_url = reverse_lazy('home')
    form_class = imageDeleteForm

