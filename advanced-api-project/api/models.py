from django.db import models

#Creation of the Author of book model 
class Author(models.Model):
    name = models.CharField(max_length=200)

#Creation of Book model with  a one-to-many relationship from Author to Books
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
