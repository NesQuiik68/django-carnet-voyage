from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Destination, Favori
from django.http import HttpResponseForbidden

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'voyages/destination_list.html', {'destinations': destinations})

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'voyages/destination_detail.html', {'destination': destination})

@login_required
def ajouter_favori(request, pk):
    if not request.user.isLoggedIn:
        return HttpResponseForbidden("Vous devez être connecté pour ajouter aux favoris.")
    destination = get_object_or_404(Destination, pk=pk)
    favori, created = Favori.objects.get_or_create(user=request.user)

    if destination in favori.destinations.all():
        favori.destinations.remove(destination)
    else:
        favori.destinations.add(destination)
    return redirect('destination_detail', pk=pk)
