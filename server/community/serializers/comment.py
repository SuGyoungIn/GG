from ..models import Comment, Article
from rest_framework import serializers
from django.contrib.auth.models import User
from .user import UserSerializer

class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title', )
    article = ArticleSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'