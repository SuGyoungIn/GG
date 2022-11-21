from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers.movies import MovieSerializer,FindMovieSerializer
from .models import Movie, Genre

@api_view(['GET'])
def movies(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies,many=True)
    for d in serializer.data:
        d.pop('vote_count')
    return Response(serializer.data)
    
@api_view(['GET'])
def movie(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
# Create your views here.

@api_view(['GET'])
def find_movie(request):
    movies = get_list_or_404(Movie)
    serializer = FindMovieSerializer(movies,many=True)
    return Response(serializer.data)

