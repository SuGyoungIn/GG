from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.movies),
    path('genres/',views.genres),
    path('search/',views.search_movie),
    path('<int:movie_pk>/',views.movie),
    path('<int:movie_pk>/comments/',views.comments),
    path('<int:movie_pk>/likes/',views.movie_likes,name="movie_likes"),
    path('get_sim_user/',views.get_sim_user)
]