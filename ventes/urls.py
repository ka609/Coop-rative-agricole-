from django.urls import path
from .views import VenteListView, VenteCreateView

urlpatterns = [
    path('', VenteListView.as_view(), name='vente-list'),  # Route pour la liste des ventes
    path('ajouter/', VenteCreateView.as_view(), name='vente-create'),  # Route pour créer une nouvelle vente
]
