from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import get_user_model
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .utils import generate_access_token, generate_refresh_token


@api_view(['GET'])
def profile(request):
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user})


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    response = Response()
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'Username and Password required')
    user = User.objects.filter(username=username).first()
    if (user is None):
        raise exceptions.AuthenticationFailed('User not found')
    if (not user.check_password(password)):
        raise exceptions.AuthenticationFailed('Wrong Password!')
    
    serialized_user = UserSerializer(user).data
    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.set_cookie(key='refreshtoken', value=refresh_token,
                        httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_user
    }

    return response


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def register_view(request):
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    if (username is None) or (password is None) or (email is None) or (first_name is None) or (last_name is None):
        raise exceptions.AuthenticationFailed(
            'All fields are required')
    serializer = UserSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
