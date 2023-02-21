from django.contrib.auth import get_user_model
from django.test import Client, TestCase

User = get_user_model()


class SmokeTest(TestCase):
    def setUp(self) -> None:
        self.guest_client = Client()
        self.user = User.objects.create_user(username='HasNoName',
                                             email='test@test.ru',
                                             password='p@ssword')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_recipes(self):
        response = self.guest_client.get('/api/recipes/')
        self.assertEqual(response.status_code, 200)

    def test_users(self):
        response = self.guest_client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_me(self):
        response = self.authorized_client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
