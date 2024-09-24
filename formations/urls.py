from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormationListView.as_view(), name='formation-list'),
    path('create/', views.FormationCreateView.as_view(), name='formation-create'),
    path('<int:pk>/', views.FormationDetailView.as_view(), name='formation-detail'),
]
