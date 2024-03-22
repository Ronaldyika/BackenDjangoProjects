from django.urls import path
from .views import movieList

urlpatterns = [
    path('',movieList,name='movielist'),
    
]
