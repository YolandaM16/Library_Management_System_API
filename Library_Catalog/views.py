from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book, Author, CustomUser, Transaction
from .serializers import BookSerializer, AuthorSerializer, CustomUserSerializer, TransactionSerializer

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