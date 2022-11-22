from ..models import Movie,Genre
from rest_framework import serializers
from django.contrib.auth.models import User
from .user import UserSerializer


class MovieSerializer(serializers.ModelSerializer):
    
    class GenresSerializers(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    genre_ids = GenresSerializers(many=True,read_only=True)
    like_users = UserSerializer(read_only=True,many=True)
    class Meta:
        model = Movie
        fields = '__all__'
        
class SearchMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','original_title','poster_path','vote_average','vote_count','release_date','genre_ids')

