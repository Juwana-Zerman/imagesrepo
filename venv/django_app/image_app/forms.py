from django import forms
from .models import Post

class imagePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image']