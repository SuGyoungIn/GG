from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers.movies import MovieSerializer,SearchMovieSerializer
from .serializers.genre import GenreSerializers
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
def genres(request):
    genres=get_list_or_404(Genre)
    serializer = GenreSerializers(genres,many=True)
    return Response(serializer.data)

@api_view(['GET'])  #비로그인, 돋보기 버튼누르면 통신
def search_movie(request):
    movies = get_list_or_404(Movie)
    serializer = SearchMovieSerializer(movies,many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def movie_likes(request,movie_pk):
    print()
    print('here!!!!!!!!!!')
    print(request.user)

    movie = get_object_or_404(Movie,pk=movie_pk)
    if request.method=='GET':
        pass
    elif request.method=='POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user.pk)
            print('Delete')
        else:
            movie.like_users.add(request.user.pk)
            print('Add')
        return Response()
    