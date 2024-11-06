from django.contrib import admin
from .models import Membre,  Formation

# Admin pour le modèle Membre
@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ['prenom', 'nom', 'email', 'telephone', 'role']
    search_fields = ['prenom', 'nom', 'email']
    list_filter = ['role']

class FormationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_creation')
    search_fields = ('titre', 'description')
    list_filter = ('date_creation',)

admin.site.register(Formation, FormationAdmin)
