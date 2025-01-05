from django.contrib import admin
from .models import Destination, Lieu, Avis, Favori

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)

@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination')
    search_fields = ('name', 'destination__name')

@admin.register(Avis)
class AvisAdmin(admin.ModelAdmin):
    list_display = ('lieu', 'note')
    search_fields = ('lieu__name', 'commentaire')

@admin.register(Favori)
class FavoriAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

