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
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method=='POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user.pk)
        else:
            print("add됨")
            movie.like_users.add(request.user.pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def comments(request,movie_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Comment,movie=movie_pk)
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        movie = get_object_or_404(Movie,pk=movie_pk)
        try:
            comments = Comment.objects.filter(movie=movie_pk)
            for comment in comments:
                if comment.user.username==request.user.username:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie,user=request.user)
                return Response(serializer.data)
        except:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie,user=request.user)
                return Response(serializer.data)


@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        if request.user == comment.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)



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
def get_sim_items(request):
    this_user=request.user.username
    users = get_list_or_404(get_user_model())
    movies = get_list_or_404(Movie)
    comments = get_list_or_404(Comment)
    columns = dict()
    row = dict()
    sim=dict()
    simsim=dict()
    for user in users:
        columns[user.username]=0
    for movie in movies:
        row[movie.id]=columns.copy()
        sim[movie.id]=0
    for movie in movies:
        simsim[movie.id]=sim.copy()

    for comment in comments:
        row[comment.movie.id][comment.user.username]+=comment.stars

    pprint(row)
    user_comments = get_list_or_404(Comment,user=request.user.pk)

    movie_list=[]
    for comment in user_comments:
        movie_list.append(comment.movie.id)

    for movie1 in movies:
        for movie2 in movies:
            if movie1.id ==movie2.id:
                simsim[movie1.id][movie2.id]=1
                continue
            if row[movie1.id]==columns or row[movie2.id]==columns:continue
            a=0
            b=0
            c=0
            for i in columns.keys():
                a+=row[movie1.id][i]*row[movie2.id][i]
                b+=row[movie1.id][i]**2
                c+=row[movie2.id][i]**2
            simsim[movie1.id][movie2.id]=a/((b**0.5)*(c**0.5))
    
    pprint(simsim)
    rec_movie_list=[]
    for movie1 in movie_list:
        s=row[movie1][request.user.username]
        for movie2 in movies:
            if movie2.id in movie_list:
                continue
            sim[movie2.id]+=s*simsim[movie1][movie2.id]

    pprint(sim)

    for key,value in sim.items():
        if value:
            this_movie=get_object_or_404(Movie,pk=key)
            rec_movie_list.append({
                'movie_id':key,
                'poster_path':this_movie.poster_path,
                'title':this_movie.title,
                'sim':value
            })
    rec_movie_list.sort(reverse=True,key=lambda x:x['sim'])
    return Response(rec_movie_list)



    
    
    
    