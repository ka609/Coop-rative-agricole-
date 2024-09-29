from django.urls import path
from . import views

urlpatterns = [
    path('membres/', views.liste_membres, name='liste_membres'),
    path('membres/<int:id>/', views.detail_membre, name='detail_membre'),
]
