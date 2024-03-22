from django.shortcuts import render
from .models import Movie

def movieList(request):
    queryset = Movie.objects.all()
    movies = list(queryset.values())

    return({'movies':movies})