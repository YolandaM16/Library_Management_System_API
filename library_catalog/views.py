from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book, Author, CustomUser, Transaction
from .serializers import BookSerializer, AuthorSerializer, CustomUserSerializer, TransactionSerializer

User = get_user_model()

# Create your views here.
class BookList(ListCreateAPIView):
    def get_queryset(self):
        return Book.object.all()
    
    def get_serializer_class(self):
        return BookSerializer
    

class BookDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Book.objects.all()
    
    def get_serializer(self):
        return BookSerializer
    

class AuthorList(ListCreateAPIView):
    def get_queryset(self):
        return Author.object.all()
    
    def get_serializer_class(self):
        return AuthorSerializer
    
class AuthorDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Author.object.all()
    
    def get_serializer_class(self):
        return AuthorSerializer
    
class CustomUserList(ListCreateAPIView):
    def get_queryset(self):
        return CustomUser.object.all()
    
    def get_serializer_class(self):
        return CustomUserSerializer
    
class CustomUserDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return CustomUser.object.all()
    
    def get_serializer_class(self):
        return CustomUserSerializer
    
class TransactionList(ListCreateAPIView):
    def get_queryset(self):
        return Transaction.object.all()
    
    def get_serializer_class(self):
        return TransactionSerializer
    
class TransactionDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Transaction.object.all()
    
    def get_serializer_class(self):
        return TransactionSerializer
    
class RegisterView(generics.CreateAPIView):
    def get_queryset(self):
        return User.object.all()
    
    def get_serializer_class(self):
        return RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        user = User.objects.get(username=response.data.get('username'))
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': response.data})


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
