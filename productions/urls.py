from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_productions, name='liste_productions'),
    path('<int:id>/', views.detail_production, name='detail_production'),
]
