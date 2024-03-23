from django.urls import path
# from .views import movieList,movieDetail,addMovie,movieDetailinfo
from .views import watchlist,watchlistdetail,streamplateformlist,streamPlateformdetails

urlpatterns = [
    # path('',movieList,name='movielist'),
    # path('<int:pk>/',movieDetail,name='moviedetail'),
    # path('addmovie/',addMovie,name='addMovie'),
    # path('addmovie/<int:pk>/',movieDetailinfo,name='info detail'),

    path('',watchlist.as_view(),name='watchlist'),
    path('<int:pk>/',watchlistdetail.as_view(),name='watchlistdetail'),
    path('platform/',streamplateformlist.as_view(),name='plateform'),
    path('platform/<int:pk>/',streamPlateformdetails.as_view(),name='platformdetails'),
    
]
