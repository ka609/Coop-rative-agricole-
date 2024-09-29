from django.urls import path
from . import views

urlpatterns = [
    path('commandes/', views.liste_commandes, name='liste_commandes'),
    path('commandes/<int:id>/', views.detail_commande, name='detail_commande'),
    path('panier/', views.detail_panier, name='detail_panier'),
    path('transactions/', views.liste_transactions, name='liste_transactions'),
]
