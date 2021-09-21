from django import forms
from django.forms import fields
from .models import Post

class imagePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image']

class imageDeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image']