from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def username(request):
    sub={
        'username':request.user.username,
        'user_pk':request.user.pk
    }
    return Response(sub)
    