from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import ExampleForm

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

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the valid form data here
            # For example, you could save it to the database or send an email
            cleaned_data = form.cleaned_data
            print(cleaned_data)  # Just for testing purposes
            return render(request, 'bookshelf/form_example.html', {'form': form, 'success': True})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
