from django.test import Client, TestCase


class SmokeTest(TestCase):
    def setUp(self) -> None:
        self.guest_client = Client()

    def test_recipes(self):
        response = self.guest_client.get('/api/recipes/')
        self.assertEqual(response.status_code, 200)

    def test_users(self):
        response = self.guest_client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
