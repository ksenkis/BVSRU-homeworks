from django.contrib import admin
from django.urls import path
from .models import Group, Post
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>/', views.group_posts),
]
