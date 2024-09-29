from django.contrib import admin
from .models import Commande, Panier, PanierProduit, Transaction

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'membre', 'produit', 'quantite', 'statut', 'date_commande', 'total')
    search_fields = ('membre__username', 'produit__nom')
    list_filter = ('statut',)

@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ('membre',)
    search_fields = ('membre__username',)

@admin.register(PanierProduit)
class PanierProduitAdmin(admin.ModelAdmin):
    list_display = ('panier', 'produit', 'quantite')
    search_fields = ('panier__membre__username', 'produit__nom')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('commande', 'montant', 'date_paiement', 'transaction_id')
    search_fields = ('commande__membre__username', 'transaction_id')

