from .models import Book, Author
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', "author"]

class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ["name"]

    def Validate(self):
        pass