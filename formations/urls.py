from django.urls import path
from . import views

urlpatterns = [
    path('formations/', views.liste_formations, name='liste_formations'),
    path('formations/<int:id>/', views.detail_formation, name='detail_formation'),
    path('formateurs/', views.liste_formateurs, name='liste_formateurs'),
    path('categories/', views.liste_categories, name='liste_categories'),
]
