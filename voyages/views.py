from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Destination, Favori, Avis
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import DestinationForm

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'voyages/destination_list.html', {'destinations': destinations})

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST' and request.user.is_authenticated and request.user.isLoggedIn:
        note = request.POST.get('note')
        commentaire = request.POST.get('commentaire')
        if note and commentaire:
            Avis.objects.create(destination=destination, note=note, commentaire=commentaire)
            messages.success(request, "Avis ajouté avec succès!")
            return redirect('destination_detail', pk=pk)
        else:
            messages.error(request, "Veuillez remplir tous les champs.")
    return render(request, 'voyages/destination_detail.html', {'destination': destination})

@login_required
def ajouter_favori(request, pk):
    if not request.user.isLoggedIn:
        return HttpResponseForbidden("Vous devez être connecté pour ajouter aux favoris.")
    destination = get_object_or_404(Destination, pk=pk)
    favori, created = Favori.objects.get_or_create(user=request.user)

    if favori:
        if destination in favori.destinations.all():
            favori.destinations.remove(destination)
        else:
            favori.destinations.add(destination)
    return redirect('destination_detail', pk=pk)

@login_required
def favoris_list(request):
    favori = Favori.objects.filter(user=request.user).first()
    if favori:
        destinations = favori.destinations.all()
    else:
        destinations = []
    return render(request, 'voyages/favoris_list.html', {'destinations': destinations})

@login_required
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
