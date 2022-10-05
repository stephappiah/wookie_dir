from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


class BaseTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/auth/registration/'
        self.login_url = '/auth/login/'
        self.books_url = reverse('books')
        self.signup_data = {
            'username': 'test',
            'email': 'tester@wookie.com',
            'password1': 'test12346&',
            'password2': 'test12346&'
        }

        self.login_data = {
            'username': 'test',
            'email': 'tester@wookie.com',
            'password': 'test12346&'
        }

        return super().setUp()


    def login(self, data):
        return self.client.post(self.login_url, data)

    def register(self, data):
        return self.client.post(self.register_url, data)

