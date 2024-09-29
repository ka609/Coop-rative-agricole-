from django.contrib import admin
from .models import Formateur, Categorie, Formation, Progression

@admin.register(Formateur)
class FormateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')
    search_fields = ('nom', 'prenom', 'email')

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_debut', 'date_fin', 'formateur', 'categorie')
    search_fields = ('titre', 'formateur__nom')
    list_filter = ('categorie',)

@admin.register(Progression)
class ProgressionAdmin(admin.ModelAdmin):
    list_display = ('membre', 'formation', 'progression')
    search_fields = ('membre__username', 'formation__titre')

