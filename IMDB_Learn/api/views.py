from django.shortcuts import render
from .models import Watchlist,StreamPlateform,Review
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import WatchlistSerializer,StreamPlateformSerializer,ReveiwSerializer
from rest_framework import generics

class watchlist(generics.ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer


class watchlistdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

class streamplateformlist(generics.ListCreateAPIView):
    queryset = StreamPlateform.objects.all()
    serializer_class = StreamPlateformSerializer


class streamPlateformdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlateform.objects.all()
    serializer_class = StreamPlateformSerializer



class reviewlist(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReveiwSerializer

    def review_user(request,pk):
        queryset = Review.objects.get(user=user)
        if queryset.DoesNotExist():
            queryset.create()
        else{
            
        }


class reviewdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReveiwSerializer







# @api_view()
# def movieList(request):
#     queryset = Movie.objects.all()
#     serializer = MovieSerializer(queryset,many=True)

#     return Response(serializer.data)

# @api_view()
# def movieDetail(request, pk):
#     queryset = Movie.objects.get(pk=pk)
#     serializer = MovieSerializer(queryset)

#     return Response(serializer.data)



# @api_view(['GET','POST'])
# def addMovie(request):
#     queryset = Movie.objects.all()
#     if request.method == 'GET':
#         serializer = MovieSerializer(queryset,many = True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

# @api_view(['PUT','DELETE'])
# def movieDetailinfo(request,pk):
#     movie = Movie.objects.get(pk=pk)

#     if request.method == 'PUT':
#         serializer = MovieSerializer(movie,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)