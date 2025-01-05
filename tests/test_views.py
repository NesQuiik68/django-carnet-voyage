<file>
      from django.test import TestCase, Client
      from django.urls import reverse
      from voyages.models import Destination, Favori
      from django.contrib.auth.models import User
      from unittest.mock import patch

      class FavoritesViewTest(TestCase):
          def setUp(self):
              self.client = Client()
              self.user = User.objects.create_user(username="testuser", password="testpassword")
              self.destination = Destination.objects.create(name="Test Destination")

          def test_add_remove_favorite(self):
              self.client.login(username="testuser", password="testpassword")
              url = reverse('ajouter_favori', kwargs={'pk': self.destination.pk})

              # Add to favorites
              response = self.client.post(url)
              self.assertEqual(response.status_code, 302)
              favori = Favori.objects.get(user=self.user)
              self.assertIn(self.destination, favori.destinations.all())

              # Remove from favorites
              response = self.client.post(url)
              self.assertEqual(response.status_code, 302)
              favori = Favori.objects.get(user=self.user)
              self.assertNotIn(self.destination, favori.destinations.all())

          def test_add_favorite_unauthenticated(self):
              url = reverse('ajouter_favori', kwargs={'pk': self.destination.pk})
              response = self.client.post(url)
              self.assertEqual(response.status_code, 302)
              self.assertFalse(Favori.objects.filter(user=self.user).exists())

      class MockResponse:
          def __init__(self, status_code, json_data):
              self.status_code = status_code
              self.json_data = json_data

          def json(self):
              return self.json_data

      class ExternalApiTest(TestCase):
          @patch('requests.get')
          def test_external_api_call(self, mock_get):
              mock_response = MockResponse(200, {'data': 'test'})
              mock_get.return_value = mock_response

              # Replace with your actual API call logic
              # For example:
              # import requests
              # response = requests.get('https://example.com/api')
              # self.assertEqual(response.status_code, 200)
              # self.assertEqual(response.json(), {'data': 'test'})

              # Mock API call
              mock_get.assert_called_once()
    </file>
