from django.urls import path
from .views import ListView

urlpatterns = [
    path('books/', ListView.as_view(), name='books-list')
]