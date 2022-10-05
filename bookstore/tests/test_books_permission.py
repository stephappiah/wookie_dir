from .common import BaseTestCase


class TestBooksPermission(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.signup_data = {
            'username': 'darth-vader',
            'email': 'tester@wookie.com',
            'password1': 'test12346&',
            'password2': 'test12346&'
        }
        register_res = self.register(self.signup_data)
        token = register_res.data['access_token']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_blacklisted_user_cannot_create_book(self):
        response = self.client.post(self.books_url, self.book_data)
        self.assertEqual(response.status_code, 403)
