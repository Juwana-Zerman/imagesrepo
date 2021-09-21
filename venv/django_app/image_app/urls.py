from django.urls import path
from . import views #imports view file
from .views import imagePageView, createPostView

urlpatterns = [
    #path("", views.home, name="home"),
    path('', imagePageView.as_view(), name='home'),
    path('post/', createPostView.as_view(), name='add_image'),
]
