book_to_delete = Book.objects.get(title='Nineteen Eighty-Four')
book_to_delete.delete()

output: (1, {'bookshelf.Book': 1})
