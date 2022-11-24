from django.db import models
from django.conf import settings


class Genre(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)

class Movie(models.Model):
    id=models.IntegerField(primary_key=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    genre_ids=models.ManyToManyField(Genre)

    title=models.CharField(max_length=100)
    original_title=models.CharField(max_length=100)

    overview=models.TextField()
    popularity=models.FloatField()

    poster_path=models.CharField(max_length=300)
    backdrop_path= models.CharField(max_length=300)

    release_date=models.DateField(auto_now=False, auto_now_add=False)
    vote_average=models.FloatField()
    vote_count= models.IntegerField()

class Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_comments")
    content = models.TextField()
    stars = models.FloatField()
    recommends = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='recommends')      
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
