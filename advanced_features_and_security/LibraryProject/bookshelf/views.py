from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

@permission_required('bookshelf.can_edit', raise_exception=True, )
def edit_book(request, title):
    book = get_object_or_404(Book, title=title)
    # Perform the edit logic here
    return render(request, 'bookshelf/edit_book.html', {'books': book})
