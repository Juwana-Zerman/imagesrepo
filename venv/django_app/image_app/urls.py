from django.urls import path
from . import views #imports view file
from .views import imagePageView

urlpatterns = [
    #path("", views.home, name="home"),
    path('', imagePageView.as_view(), name='home')
]
