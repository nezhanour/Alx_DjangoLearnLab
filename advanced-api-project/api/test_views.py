from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from datetime import date
from rest_framework.test import APIClient

class BookAPITestCase(APITestCase):
    
    def setUp(self):
        """Set up initial data for the tests."""
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name="Author A")
        self.book1 = Book.objects.create(title="Book 1", publication_year="2020-01-01", author=self.author)
        self.book2 = Book.objects.create(title="Book 2", publication_year="2021-01-01", author=self.author)
        self.book3 = Book.objects.create(title="Book 3", publication_year="2019-01-01", author=self.author)
        
        # URLs
        self.list_url = reverse('books-list')
        self.create_url = reverse('books-create')
        self.detail_url = reverse('books-retrieve', kwargs={'pk': self.book1.id})
    
    # Test Create API
    def test_create_book(self):
        """Test that a book can be created via the API."""
        data = {
            "title": "New Book",
            "publication_year": "2022-01-01",
            "author_name": "New Author"
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)  # Check if the book count increased
        
    # Test List API
    def test_list_books(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # We have 3 books in setUp
        
    # Test Retrieve API
    def test_retrieve_book(self):
        """Test retrieving a single book."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
        
    # Test Update API
    def test_update_book(self):
        """Test updating a book's title."""
        update_url = reverse('books-update', kwargs={'pk': self.book1.id})
        data = {"title": "Updated Book 1", "publication_year": "2020-01-01", "author_name": "Author A"}
        response = self.client.put(update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book 1")
    
    # Test Delete API
    def test_delete_book(self):
        """Test deleting a book."""
        delete_url = reverse('books-delete', kwargs={'pk': self.book1.id})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

        # Test filtering by title
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {'title': 'Book 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book 1')
    
    # Test searching by author name
    def test_search_books_by_author(self):
        response = self.client.get(self.list_url, {'search': 'Author A'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # All books by Author A
    
    # Test ordering by publication year
    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], "2019-01-01")  # Oldest book first

    # Test authenticated access to create
    def test_authenticated_create_book(self):
        # Log in as the user
        self.client.login(username='testuser', password='testpass')

        # Now, create a book as an authenticated user
        data = {
            "title": "New Authenticated Book",
            "publication_year": "2022-01-01",
            "author_name": "New Author"
        }
        response = self.client.post(self.book_url, data, format='json')

        # Check if the book is created successfully (status code 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test unauthenticated access to create
    def test_unauthenticated_create_book(self):
        # Try to create a book without logging in
        data = {
            "title": "Unauthenticated Book",
            "publication_year": "2022-01-01",
            "author_name": "New Author"
        }
        response = self.client.post(self.book_url, data, format='json')

        # Check if the request is forbidden (status code 403)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
