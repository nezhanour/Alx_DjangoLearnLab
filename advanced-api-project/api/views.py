from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Book
from .serializers import BookSerializer

class ListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView (DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer