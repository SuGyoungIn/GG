from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie,Comment
class UserSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
    like_movies= MovieSerializer(read_only=True,many=True)

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
    user_comments = CommentSerializer(read_only=True,many=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'