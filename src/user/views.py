from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from user.serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def registration(request: Request) -> Response:
    username = request.data.get('username')
    try:
        User.objects.get(username=username)
        return Response(data={'message': 'user already exists'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        user = User()
        user.username = username
        user.set_password(raw_password=request.data.get('password'))
        user.verified = request.data.get('verified', True)
        user.profile_pic_url = request.data.get('profile_pic_url')
        user.address = request.data.get('address')
        user.gender = request.data.get('gender', 'male')
        user.is_superuser = request.data.get('is_superuser', False)
        user.is_staff = request.data.get('is_staff', False)
        user.first_name = request.data.get('first_name', False)
        user.last_name = request.data.get('last_name', False)
        user.save()
        return Response(data={'data': UserSerializer(user).data}, status=status.HTTP_201_CREATED)
