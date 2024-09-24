from django.urls import path
from .views import ProductionListView, ProductionCreateView

urlpatterns = [
    path('', ProductionListView.as_view(), name='production-list'),
    path('ajouter/', ProductionCreateView.as_view(), name='production-create'),  # Nouvelle route pour créer une production
]
