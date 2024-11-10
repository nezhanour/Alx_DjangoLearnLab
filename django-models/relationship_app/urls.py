from django.urls import path
from . import views

urlpatterns = [
    # URL patterns that route to the Function-based view to list all books
    path('books/', views.book_list, name='book_list'),

    # URL patterns that route to the Class-based view to show a library's details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail')
]