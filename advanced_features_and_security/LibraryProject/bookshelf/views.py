from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

@permission_required('bookshelf.can_edit', raise_exception=True, )
def edit_book(request, title):
    book_list = get_object_or_404(Book, title=title)
    # Perform the edit logic here
    return render(request, 'bookshelf/edit_book.html', {'books': book_list})

def search_books(request):
    query = request.GET.get('q', '')
    if query:
        # Securely filter books using Django ORM
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    
    return render(request, 'bookshelf/book_list.html', {'books': books})
