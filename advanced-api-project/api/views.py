from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters import rest_framework 

class ListView(generics.ListAPIView):
    queryset = Book.objects.all() # All books in the database
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # Filter by title, author's name, and publication year
    filterset_fields = ['title', 'author', 'publication_year']
    # Search by book title or author name
    search_fields = ['title', "author__name"]
    # Allow ordering by title and publication year
    ordering_fields = ['title', 'publication_year']

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all() # All books in the database
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all() # All books in the database
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView (generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]