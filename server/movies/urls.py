from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.movies),
    path('<int:movie_pk>/',views.movie),
]