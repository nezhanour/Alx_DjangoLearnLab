from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create authors and books for testing
        self.author1 = Author.objects.create(name='John Doe')
        self.author2 = Author.objects.create(name='Jane Doe')

        Book.objects.create(title='Django for Beginners', publication_year='2020-01-01', author=self.author1)
        Book.objects.create(title='Advanced Django', publication_year='2021-05-10', author=self.author2)

    def test_filter_books_by_title(self):
        response = self.client.get('/books/', {'title': 'Django for Beginners'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Django for Beginners')

    def test_search_books_by_author(self):
        response = self.client.get('/books/', {'search': 'Jane'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Jane Doe')

    def test_order_books_by_publication_year(self):
        response = self.client.get('/books/', {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Advanced Django')