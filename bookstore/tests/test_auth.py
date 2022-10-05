from .common import BaseTestCase


class TestAuth(BaseTestCase):

    def register(self, data):
        return self.client.post(self.register_url, data)

    def test_registration(self):
        response = self.register(self.signup_data)
        self.assertEqual(response.status_code, 201)

    def test_successful_registrations_returns_token(self):
        response = self.register(self.signup_data)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

    def test_registration_with_invalid_data_fails(self):
        data = self.signup_data.copy()
        data['password1'] = 'wrong'
        response = self.register(data)
        self.assertEqual(response.status_code, 400)

    def login(self, data):
        return self.client.post(self.login_url, data)

    def test_login(self):
        self.register(self.signup_data)
        response = self.login(self.login_data)
        self.assertEqual(response.status_code, 200)

    def test_successful_login_returns_token(self):
        self.register(self.signup_data)
        response = self.login(self.login_data)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

    def test_login_with_invalid_data_fails(self):
        self.register(self.signup_data)
        data = self.login_data.copy()
        data['password'] = 'wrong'
        response = self.login(data)
        self.assertEqual(response.status_code, 400)
