from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.movies),
    path('search/',views.search_movie),
    path('<int:movie_pk>/',views.movie),
    path('<int:movie_pk>/likes/',views.movie_likes,name="movie_likes")
]