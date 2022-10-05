from .common import BaseTestCase
from rest_framework.test import APIClient


class TestBooks(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.register(self.signup_data)
        login_res = self.login(self.login_data)
        data = login_res.data
        token = data['access_token']
        self.author_id = data['user']['pk']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def create_book(self, data):
        return self.client.post(self.books_url, data)

    def test_create_book(self):
        response = self.create_book(self.book_data)
        self.assertEqual(response.status_code, 201)

    def test_successful_create_book_returns_book(self):
        response = self.create_book(self.book_data)
        self.assertIn('id', response.data)
        self.assertIn('title', response.data)
        self.assertIn('description', response.data)
        self.assertIn('price', response.data)
        self.assertIn('cover', response.data)

    def test_book_author_is_current_user(self):
        response = self.create_book(self.book_data)
        self.assertEqual(response.data['author'], self.author_id)

    def test_create_book_with_invalid_data_fails(self):
        data = self.book_data.copy()
        data['price'] = 'wrong-data-type'
        response = self.create_book(data)
        self.assertEqual(response.status_code, 400)

    def test_fetch_books(self):
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, 200)

    def test_fetch_books_authenticated(self):
        bad_client = APIClient()
        response = bad_client.get(self.books_url)
        self.assertEqual(response.status_code, 200)

    def test_fetch_books_schema(self):
        self.create_book(self.book_data)
        response = self.client.get(self.books_url)
        queryset = response.data
        data = queryset[0]
        self.assertIsInstance(queryset, list)
        self.assertIn('id', data)
        self.assertIn('title', data)
        self.assertIn('description', data)
        self.assertIn('price', data)
        self.assertIn('cover', data)
        self.assertIn('author', data)

    def test_update_book(self):
        response = self.create_book(self.book_data)
        book_id = response.data['id']
        update_url = f'{self.books_url}{book_id}/'
        data = self.book_data.copy()
        data['title'] = 'updated'
        response = self.client.patch(update_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'updated')

    def test_retrieve_book(self):
        response = self.create_book(self.book_data)
        book_id = response.data['id']
        retrieve_url = f'{self.books_url}{book_id}/'
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_delete_book(self):
        response = self.create_book(self.book_data)
        book_id = response.data['id']
        delete_url = f'{self.books_url}{book_id}/'
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, 204)
