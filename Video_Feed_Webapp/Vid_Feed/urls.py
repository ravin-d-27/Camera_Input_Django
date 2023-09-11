
from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.display_render, name='video_feed'),
    
]
