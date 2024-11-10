from django.shortcuts import render
from .models import Book

# Function-based view to list all books and their authors
def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)
