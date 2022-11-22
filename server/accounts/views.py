from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def username(request):
    sub={
        'username':request.user.username,
        'user_pk':request.user.pk
    }
    return Response(sub)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_like_movie(request,user_pk):
    user= get_object_or_404(get_user_model(),pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)