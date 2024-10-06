from django.contrib import admin
from .models import Membre

@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ('username', 'nom', 'prenom', 'email','role', 'date_inscription')
    search_fields = ('username', 'nom', 'prenom', 'email')
    list_filter = ('role',)

