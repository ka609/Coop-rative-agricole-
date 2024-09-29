from django.urls import path
from . import views

urlpatterns = [
    path('productions/', views.liste_productions, name='liste_productions'),
    path('productions/<int:id>/', views.detail_production, name='detail_production'),
]
