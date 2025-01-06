from django.test import TestCase, Client
from django.urls import reverse
from voyages.models import Destination, Favori, Avis
from django.contrib.auth.models import User
from unittest.mock import patch
from voyages.forms import DestinationForm
from django.contrib.auth.forms import AuthenticationForm

class FavoritesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword", isLoggedIn=True)
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
        self.assertEqual(response.status_code, 403)
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

        # Mock API call
        mock_get.assert_called_once()

class DestinationCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword", isLoggedIn=True)
        self.client.login(username="testuser", password="testpassword")

    def test_destination_create_form_valid(self):
        url = reverse('destination_create')
        data = {'name': 'Test Destination', 'description': 'Test Description', 'status': 'to_visit'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Destination.objects.filter(name='Test Destination').exists())

    def test_destination_create_form_invalid(self):
        url = reverse('destination_create')
        data = {'name': '', 'description': 'Test Description', 'status': 'to_visit'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Destination.objects.filter(name='').exists())
        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())

class DestinationDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword", isLoggedIn=True)
        self.client.login(username="testuser", password="testpassword")
        self.destination = Destination.objects.create(name="Test Destination")

    def test_destination_detail_view_get(self):
        url = reverse('destination_detail', kwargs={'pk': self.destination.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('destination', response.context)
        self.assertEqual(response.context['destination'], self.destination)

    def test_destination_detail_add_avis_valid(self):
        url = reverse('destination_detail', kwargs={'pk': self.destination.pk})
        data = {'note': 5, 'commentaire': 'Test Commentaire'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Avis.objects.filter(commentaire='Test Commentaire').exists())

    def test_destination_detail_add_avis_invalid(self):
        url = reverse('destination_detail', kwargs={'pk': self.destination.pk})
        data = {'note': '', 'commentaire': 'Test Commentaire'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Avis.objects.filter(commentaire='Test Commentaire', note='').exists())

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_login_view_valid(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.get(username='testuser').isLoggedIn)

    def test_login_view_invalid(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.get(username='testuser').isLoggedIn)
        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())
