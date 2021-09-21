from django.urls import path
from . import views #imports view file

urlpatterns = [
    path("", views.home, name="home"),
]
