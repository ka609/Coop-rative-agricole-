from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    #path('', views.index, name='index'),  # Si tu as une vue d'accueil (index)
]
