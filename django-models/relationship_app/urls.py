from django.urls import path
from .views import list_books, LibraryDetailView
#from . import views


urlpatterns = [
    # URL patterns that route to the Function-based view to list all books
    path('books/', list_books, name='book_list'),

    # URL patterns that route to the Class-based view to show a library's details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail')
]