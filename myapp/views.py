from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .serializers import UserSerializer, LoginSerializer

@api_view(['POST'])
def register(request):
    """
    User registration API view.

    Registers a new user with provided username, email, and password.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    """
    User login API view.

    Authenticates user with provided username/email and password, and returns JWT token on successful login.
    """
    serializer = LoginSerializer(data= request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        # Generate JWT token or perform any additional actions
        return Response({ 'user_id': user.id, 'user_email': user.email, 'token': str(refresh.access_token),}, status=status.HTTP_200_OK)
    
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)