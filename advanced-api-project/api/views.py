from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class ListView(ListAPIView):
    queryset = Book
    serializer_class = BookSerializer