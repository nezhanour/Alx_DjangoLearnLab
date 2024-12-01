from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class ListView(ListAPIView):
    queryset = Book.objects.all() # All books in the database
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DetailView(RetrieveAPIView):
    queryset = Book.objects.all() # All books in the database
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(CreateAPIView):
    queryset = Book.objects.all() # All books in the database
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView (DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]