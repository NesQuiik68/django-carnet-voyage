from django.urls import path
from . import views

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('<int:pk>/', views.destination_detail, name='destination_detail'),
    path('<int:pk>/favori/', views.ajouter_favori, name='ajouter_favori'),
    path('favoris/', views.favoris_list, name='favoris_list'),
    path('create/', views.destination_create, name='destination_create'),
]
