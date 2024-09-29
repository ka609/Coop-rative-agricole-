from django.contrib import admin
from .models import ProduitAgricole

@admin.register(ProduitAgricole)
class ProduitAgricoleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'quantite_disponible', 'prix_unitaire', 'date_ajout')
    search_fields = ('nom',)
    list_filter = ('date_ajout',)

