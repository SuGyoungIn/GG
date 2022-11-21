from django.db import models
<<<<<<< HEAD
=======
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

>>>>>>> 28f47a7a3d146643591567f44f16f45df334d80a

# Create your models here.
