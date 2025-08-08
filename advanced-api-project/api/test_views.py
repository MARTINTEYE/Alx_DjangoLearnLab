from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authentication tests
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

        # Sample books for list/search/filter tests
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author="William S. Vincent",
            description="A beginner's guide to Django.",
            publication_year=2021
        )
        self.book2 = Book.objects.create(
            title="Two Scoops of Django",
            author="Daniel Roy Greenfeld",
            description="Best practices for Django.",
            publication_year=2020
        )

        self.list_url = reverse('book-list')  # /books/
        self.detail_url = reverse('book-detail', args=[self.book1.id])  # /books/<id>/

    def test_list_books(self):
        """Ensure we can list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """Ensure we can get a single book by ID"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        """Ensure authenticated user can create a book"""
        data = {
            "title": "Test Driven Development with Django",
            "author": "Harry Percival",
            "description": "Learn TDD with Django.",
            "publication_year": 2022
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated user cannot create a book"""
        self.client.logout()
        data = {
            "title": "Unauthorized Book",
            "author": "Unknown",
            "description": "Should not be created",
            "publication_year": 2022
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Ensure authenticated user can update a book"""
        data = {
            "title": "Updated Django for Beginners",
            "author": self.book1.author,
            "description": self.book1.description,
            "publication_year": self.book1.publication_year
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django for Beginners")

    def test_delete_book_authenticated(self):
        """Ensure authenticated user can delete a book"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        """Ensure filtering by author works"""
        response = self.client.get(self.list_url, {'author': 'Daniel Roy Greenfeld'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book2.title)

    def test_search_books(self):
        """Ensure search functionality works"""
        response = self.client.get(self.list_url, {'search': 'Beginners'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    def test_order_books_by_year(self):
        """Ensure ordering works"""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
