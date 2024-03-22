from django.shortcuts import render
from .models import Movie
from rest_framework import response
from django.http import JsonResponse

def movieList(request):
    queryset = Movie.objects.all()
    data = {
        'movies':list(queryset.values())
    }


    return JsonResponse(data)

def movieDetail(request, pk):
    queryset = Movie.objects.get(pk=pk)
    data = {
        'name': queryset.name,
        'description':queryset.description,
        'isActive':queryset.isActive,
    }

    return JsonResponse(data)