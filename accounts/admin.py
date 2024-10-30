from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Personnalise l'administration du modèle User ici si nécessaire
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# Remplace l'enregistrement par défaut avec ta personnalisation
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
