from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.response import Response
from django.utils import timezone

# Create your views here.
class createUserView(generics.CreateAPIView):
    model = CustomUser
    serializer_class = UserSerializer

class loginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user:
            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},status= status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status= status.HTTP_400_BAD_REQUEST)

