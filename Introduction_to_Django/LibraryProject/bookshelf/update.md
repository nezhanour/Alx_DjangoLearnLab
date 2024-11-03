book = Book.objects.filter(title='1984')
book.update(title='Nineteen Eighty-Four')

output: 1
