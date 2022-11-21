from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.movies),
    path('find/',views.find_movie),
    path('<int:movie_pk>/',views.movie),
]