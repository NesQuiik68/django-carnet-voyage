from django.test import TestCase
from voyages.models import Destination, Lieu, Favori, Tag
from django.contrib.auth.models import User

class DestinationModelTest(TestCase):
    def test_create_destination(self):
        destination = Destination.objects.create(name="Test Destination", description="Test Description", status="to_visit")
        self.assertEqual(destination.name, "Test Destination")
        self.assertEqual(destination.description, "Test Description")
        self.assertEqual(destination.status, "to_visit")

    def test_destination_str(self):
        destination = Destination.objects.create(name="Test Destination")
        self.assertEqual(str(destination), "Test Destination")

    def test_is_visited(self):
        destination_to_visit = Destination.objects.create(name="Test Destination", status="to_visit")
        destination_visited = Destination.objects.create(name="Test Destination Visited", status="visited")
        self.assertFalse(destination_to_visit.is_visited())
        self.assertTrue(destination_visited.is_visited())

class LieuModelTest(TestCase):
    def setUp(self):
        self.destination = Destination.objects.create(name="Test Destination")

    def test_create_lieu(self):
        lieu = Lieu.objects.create(name="Test Lieu", description="Test Lieu Description", destination=self.destination)
        self.assertEqual(lieu.name, "Test Lieu")
        self.assertEqual(lieu.description, "Test Lieu Description")
        self.assertEqual(lieu.destination, self.destination)

    def test_lieu_str(self):
        lieu = Lieu.objects.create(name="Test Lieu", destination=self.destination)
        self.assertEqual(str(lieu), "Test Lieu")

class FavoriModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.destination1 = Destination.objects.create(name="Test Destination 1")
        self.destination2 = Destination.objects.create(name="Test Destination 2")

    def test_create_favori(self):
        favori = Favori.objects.create(user=self.user)
        favori.destinations.add(self.destination1)
        self.assertEqual(favori.user, self.user)
        self.assertIn(self.destination1, favori.destinations.all())

    def test_favori_str(self):
        favori = Favori.objects.create(user=self.user)
        self.assertEqual(str(favori), "Favoris de testuser")

    def test_add_remove_destination(self):
        favori = Favori.objects.create(user=self.user)
        favori.destinations.add(self.destination1)
        self.assertIn(self.destination1, favori.destinations.all())
        favori.destinations.remove(self.destination1)
        self.assertNotIn(self.destination1, favori.destinations.all())

    def test_get_favorite_count(self):
        favori = Favori.objects.create(user=self.user)
        self.assertEqual(favori.get_favorite_count(), 0)
        favori.destinations.add(self.destination1)
        self.assertEqual(favori.get_favorite_count(), 1)
        favori.destinations.add(self.destination2)
        self.assertEqual(favori.get_favorite_count(), 2)
