from rest_framework.test import APITestCase, APIClient


class BaseTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/auth/registration/'
        self.login_url = '/auth/login/'
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

