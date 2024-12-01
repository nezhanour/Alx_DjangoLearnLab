from .models import Book, Author
from rest_framework import serializers
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', "author"]

    def Validate(self, data):
        datenow = date.today()
        if 'publication_year' in data:
            if data['publication_year'] > datenow:
                raise serializers.ValidationError('Puplication date cannot be in the Future')
        return super(BookSerializer, self).validate(data)

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']