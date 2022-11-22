from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers.movies import MovieSerializer,SearchMovieSerializer
from .serializers.genre import GenreSerializers
from .serializers.comment import CommentSerializer
from django.contrib.auth import get_user_model
from .models import Movie, Genre, Comment
from pprint import pprint

@api_view(['GET'])
def movies(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

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
@permission_classes([IsAuthenticated])
def movie_likes(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    if request.method=='GET':
        pass
    elif request.method=='POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user.pk)
        else:
            movie.like_users.add(request.user.pk)
        return Response(status=status.HTTP_200_OK)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def comments(request,movie_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Comment,movie=movie_pk)
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        movie = get_object_or_404(Movie,pk=movie_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie,user=request.user)
            return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_sim_user(request):
    users = get_list_or_404(get_user_model())
    movies = get_list_or_404(Movie)
    genres = get_list_or_404(Genre)
    idc=dict()
    sim=dict()
    cos_sim=dict()
    for movie in movies:idc[movie.pk]=0
    for genre in genres:idc[genre.name]=0
    for user in users:
        sim[user.username]=idc.copy()
        cos_sim[user.username]=0
    for movie in movies:
        for user in movie.like_users.all():
            sim[user.username][movie.pk]+=10
            for genre in movie.genre_ids.all():
                sim[user.username][genre.name]+=1
    
    this_user=request.user.username
    for key in sim.keys():
        if this_user==key:continue
        if sim[key]==idc:cos_sim[key]=0;continue
        a=0
        b=0
        c=0
        for i in sim[key]:
            a+=sim[key][i]*sim[this_user][i]
            b+=sim[key][i]**2
            c+=sim[this_user][i]**2
        cos_sim[key]=a/((b**0.5)*(c**0.5))
    rec=[]
    for key,value in cos_sim.items():
        if value:
            rec.append({'username':key,'cs':value})
    rec.sort(reverse=True,key=lambda x:x['cs'])
    return Response(rec)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_sim_items(request,):
    pass