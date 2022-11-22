from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.username),
    path('<int:user_pk>/',views.user_like_movie)
]