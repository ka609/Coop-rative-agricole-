from django.urls import path
from . import views

app_name='Gestions'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('support/', views.support, name='support'),
    path('forum/', views.forum, name='forum'),
    path('legal/', views.legal, name='legal'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:discussion_id>/message/send/', views.send_message, name='send_message'),
    path('<int:message_id>/edit/', views.edit_message, name='edit_message'),
    path('<int:message_id>/delete/', views.delete_message, name='delete_message'),
    path('<int:message_id>/reply/', views.reply_message, name='reply_message'),
    path('<int:discussion_id>/', views.discussion_detail, name='discussion_detail'),
    path('discussion/create/', views.create_discussion, name='create_discussion'),

    # URLs pour la gestion des membres
    path('membres/', views.MembreListView.as_view(), name='membre_list'),  # Liste des membres
    path('membres/<int:pk>/', views.MembreDetailView.as_view(), name='membre_detail'),  # Détail d'un membre
    path('membres/ajouter/', views.MembreCreateView.as_view(), name='membre_create'),  # Ajout d'un membre
    path('membres/<int:pk>/modifier/', views.MembreUpdateView.as_view(), name='membre_update'),  # Modification d'un membre
    path('membres/<int:pk>/supprimer/', views.MembreDeleteView.as_view(), name='membre_delete'),  # Suppression d'un membre

    # URLs pour le suivi des productions
    path('productions/', views.ProductionListView.as_view(), name='production_list'),  # Liste des productions
    path('productions/<int:pk>/', views.ProductionDetailView.as_view(), name='production_detail'),  # Détail d'une production
    path('productions/ajouter/', views.ProductionCreateView.as_view(), name='production_create'),  # Ajout d'une production
    path('productions/<int:pk>/modifier/', views.ProductionUpdateView.as_view(), name='production_update'),  # Modification d'une production
    path('productions/<int:pk>/supprimer/', views.ProductionDeleteView.as_view(), name='production_delete'),  # Suppression d'une production

    # URLs pour l'e-commerce (produits)
    path('produits/', views.ProduitListView.as_view(), name='produit_list'),  # Liste des produits
    path('produits/<int:pk>/', views.ProduitDetailView.as_view(), name='produit_detail'),  # Détail d'un produit
    path('produits/ajouter/', views.ProduitCreateView.as_view(), name='produit_create'),  # Ajout d'un produit
    path('produits/<int:pk>/modifier/', views.ProduitUpdateView.as_view(), name='produit_update'),  # Modification d'un produit
    path('produits/<int:pk>/supprimer/', views.ProduitDeleteView.as_view(), name='produit_delete'),  # Suppression d'un produit

    # URLs pour la formation en ligne
    path('formations/', views.FormationListView.as_view(), name='formation_list'),  # Liste des formations
    #path('formations/<int:pk>/', views.FormationDetailView.as_view(), name='formation_detail'),  # Détail d'une formation
    path('formations/ajouter/', views.FormationCreateView.as_view(), name='formation_create'),  # Ajout d'une formation
    #path('formations/<int:pk>/modifier/', views.FormationUpdateView.as_view(), name='formation_update'),  # Modification d'une formation
    #path('formations/<int:pk>/supprimer/', views.FormationDeleteView.as_view(), name='formation_delete'),  # Suppression d'une formation


    path('commandes/', views.CommandeListView.as_view(), name='commande_list'),
    path('commandes/nouveau/', views.CommandeCreateView.as_view(), name='commande_create'),
path('commandes/<int:pk>/modifier/', views.CommandeUpdateView.as_view(), name='commande_update'),
    path('commandes/<int:pk>/', views.CommandeDetailView.as_view(), name='commande_detail'),
    path('commandes/<int:pk>/supprimer/', views.CommandeDeleteView.as_view(), name='commande_delete'),

    # URLs pour les tutoriels
    path('tutoriels/', views.TutorielListView.as_view(), name='tutoriel_list'),
    path('tutoriels/nouveau/', views.TutorielCreateView.as_view(), name='tutoriel_create'),
]
