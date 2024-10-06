from django.urls import path
from . import views

app_name = 'formations'

urlpatterns = [
    path('', views.liste_formations, name='liste_formations'),  # Liste des formations
    path('<int:formation_id>/', views.detail_formation, name='detail_formation'),  # Détails d'une formation
    path('<int:formation_id>/quiz/', views.prendre_quiz, name='prendre_quiz'),  # Prendre un quiz
]

