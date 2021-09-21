from django.urls import path
from django.views.generic.edit import DeleteView
from . import views #imports view file
from .views import deletePostView, imagePageView, createPostView

urlpatterns = [
    #path("", views.home, name="home"),
    path('', imagePageView.as_view(), name='home'),
    path('post/', createPostView.as_view(), name='add_image'),
    path('delete/<str:pk>', deletePostView.as_view(), name='delete_image'),
]
