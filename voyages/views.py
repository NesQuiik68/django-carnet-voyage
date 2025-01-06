from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Destination, Favori, Avis
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import DestinationForm
from django.conf import settings
import requests
from django.utils import timezone
from users.decorators import login_required_custom

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'voyages/destination_list.html', {'destinations': destinations})

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST' and request.user.is_authenticated and request.user.isLoggedIn:
        note = request.POST.get('note')
        commentaire = request.POST.get('commentaire')
        if note and commentaire:
            Avis.objects.create(destination=destination, note=note, commentaire=commentaire, user=request.user)
            messages.success(request, "Avis ajouté avec succès!")
            return redirect('destination_detail', pk=pk)
        else:
            messages.error(request, "Veuillez remplir tous les champs.")
    
    city = destination.name
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fr'
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
    except requests.exceptions.RequestException as e:
        weather_data = None
        messages.error(request, f"Erreur lors de la récupération des données météo: {e}")
    
    return render(request, 'voyages/destination_detail.html', {'destination': destination, 'weather_data': weather_data})

@login_required_custom
def ajouter_favori(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    favori, created = Favori.objects.get_or_create(user=request.user)

    if favori:
        if destination in favori.destinations.all():
            favori.destinations.remove(destination)
        else:
            favori.destinations.add(destination)
    
    if created or destination not in favori.destinations.all():
        favori.date_added = timezone.now()
        favori.save()
    return redirect('destination_detail', pk=pk)

@login_required_custom
def favoris_list(request):
    favori = Favori.objects.filter(user=request.user).first()
    if favori:
        destinations = favori.destinations.all()
    else:
        destinations = []
    return render(request, 'voyages/favoris_list.html', {'destinations': destinations})

@login_required_custom
def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Destination ajoutée avec succès!")
            return redirect('destination_list')
        else:
            messages.error(request, "Veuillez corriger les erreurs du formulaire.")
    else:
        form = DestinationForm()
    return render(request, 'voyages/destination_form.html', {'form': form})

def weather_view(request):
    city = 'Strasbourg'
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fr'
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
    except requests.exceptions.RequestException as e:
        weather_data = None
        messages.error(request, f"Erreur lors de la récupération des données météo: {e}")
    return render(request, 'voyages/weather.html', {'weather_data': weather_data})
