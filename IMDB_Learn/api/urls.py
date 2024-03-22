from django.urls import path
from .views import movieList,movieDetail

urlpatterns = [
    path('',movieList,name='movielist'),
    path('<int:pk>/',movieDetail,name='moviedetail'),
    
]
