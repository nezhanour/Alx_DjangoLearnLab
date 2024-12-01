from .models import Book, Author
from rest_framework import serializers
from datetime import date

#A BookSerializer that serializes all fields of the Book model with a custom validation to ensure the publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(write_only=True)  # Accept author name instead of ID
    author = serializers.StringRelatedField(read_only=True)  # To show author name in responses

    class Meta:
        model = Book
        fields = ['title', 'publication_year', "author", 'author_name']

    # Custom validation to ensure publication year is not in the future
    def Validate(self, data):
        datenow = date.today()
        if 'publication_year' in data and data['publication_year'] > datenow:
                raise serializers.ValidationError('Puplication date cannot be in the Future')
        return data
    
    # Override create to handle the author creation
    def create(self, validated_data):
        # Extract the author name from the validated data
        author_name = validated_data.pop('author_name')

        # Check if the author already exists, otherwise create a new one
        author, created = Author.objects.get_or_create(name=author_name)

        # Now create the book with the found/created author
        book = Book.objects.create(author=author, **validated_data)
        return book
    
    # For updating the book, we can handle it similarly
    def update(self, instance, validated_data):
        author_name = validated_data.pop('author_name', None)
        if author_name:
            # Find or create the author if a new author_name is provided
            author, created = Author.objects.get_or_create(name=author_name)
            instance.author = author
        
        # Update other fields
        instance.title = validated_data.get('title', instance.title)
        instance.publication_year = validated_data.get('publication_year', instance.publication_year)
        instance.save()
        return instance

#An AuthorSerializer that serializes all fields of the Author mode with a nested BookSerializer to serialize the related books dynamically
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']