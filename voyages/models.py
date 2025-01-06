from django.db import models
from django.conf import settings
from django.utils import timezone

class Destination(models.Model):
    STATUS_CHOICES = [
        ('to_visit', 'À visiter'),
        ('visited', 'Visité'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_visit')

    def __str__(self):
        return self.name

    def is_visited(self):
        return self.status == 'visited'

class Lieu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='lieux')

    def __str__(self):
        return self.name

class Avis(models.Model):
    note = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    commentaire = models.TextField(blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='avis', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True) # Added user field

    def __str__(self):
        if self.destination:
            return f"Avis pour {self.destination.name} - Note: {self.note}"
        else:
            return f"Avis sans destination - Note: {self.note}"

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Favori(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favoris')
    destinations = models.ManyToManyField(Destination, related_name='favoris', blank=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Favoris de {self.user.username}"

    def get_favorite_count(self):
        return self.destinations.count()

class DestinationTag(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('destination', 'tag')
