from django.contrib import admin
from .models import Formation

class FormationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'type_formation', 'date_publication')
    list_filter = ('type_formation', 'date_publication')
    search_fields = ('titre', 'description')

admin.site.register(Formation, FormationAdmin)
