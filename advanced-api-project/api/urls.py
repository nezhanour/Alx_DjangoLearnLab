from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('books/', ListView.as_view(), name='books-list'),
    path('books/<pk>/', DetailView.as_view(), name='books-retrieve'),
    path('books/create', CreateView.as_view(), name='books-create'),
    path('books/update', UpdateView.as_view(), name='books-update'),
    path('books/delete', DeleteView.as_view(), name='books-delete'),
]