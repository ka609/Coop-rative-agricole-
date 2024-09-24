from django.urls import path
from . import views

urlpatterns = [
    path('', views.MembreListView.as_view(), name='membre-list'),
    path('create/', views.MembreCreateView.as_view(), name='membre-create'),
    path('<int:pk>/', views.MembreDetailView.as_view(), name='membre-detail'),
]
