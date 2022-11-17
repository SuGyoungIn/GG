from django.db import models



class Genre(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)

class Movie(models.Model):
    backdrop_path= models.CharField(max_length=300)
    genre_ids=models.ManyToManyField(Genre)
    id=models.IntegerField(primary_key=True)
    original_title=models.CharField(max_length=100)
    overview=models.TextField()
    popularity=models.FloatField()
    poster_path=models.CharField(max_length=300)
    release_date=models.DateField(auto_now=False, auto_now_add=False)
    title=models.CharField(max_length=100)
    vote_average=models.FloatField()
    vote_count= models.IntegerField()




# Create your models here.
