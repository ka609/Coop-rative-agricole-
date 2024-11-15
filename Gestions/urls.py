from django.urls import path
from . import views

app_name='Gestions'

urlpatterns = [
    path('', views.index, name='index'),
    #path('create-invoice/', views.create_invoice_view, name='create-invoice'),
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
    path('articles/', views.liste_articles, name='liste_articles'),
    path('ecommerce/', views.ecommerce, name='ecommerce'),
    path('acheter/<int:article_id>/', views.acheter_article, name='acheter_article'),  # URL pour commander un article
    path('article/<int:article_id>/', views.detail_article, name='detail_article'),
    path('publier_article/', views.publier_article, name='publier_article'),
    path('cinetpay_webhook/', views.cinetpay_webhook, name='cinetpay_webhook'),
    path('creer_facture/<int:article_id>/', views.creer_facture, name='creer_facture'),
    path('article/supprimer/<int:article_id>/', views.supprimer_article, name='supprimer_article'),
    # URLs pour la gestion des membres
    path('membres/', views.MembreListView.as_view(), name='membre_list'),  # Liste des membres
    path('membres/<int:pk>/', views.MembreDetailView.as_view(), name='membre_detail'),  # Détail d'un membre
    path('membres/ajouter/', views.MembreCreateView.as_view(), name='membre_create'),  # Ajout d'un membre
    path('membres/<int:pk>/modifier/', views.MembreUpdateView.as_view(), name='membre_update'),  # Modification d'un membre
    path('membres/<int:pk>/supprimer/', views.MembreDeleteView.as_view(), name='membre_delete'),  # Suppression d'un membre

    path('formations/', views.liste_formations, name='liste_formations'),
    path('formations/<int:formation_id>/', views.detail_formation, name='detail_formation'),
    path('formations/creer/', views.creer_formation, name='creer_formation'),
    path('suivi_agricole/', views.suivi_agricole, name='suivi_agricole'),
    path('ajouter_commentaire/', views.ajouter_commentaire, name='ajouter_commentaire'),
    path('formations/supprimer/<int:id>/', views.supp_formation, name='supp_formation'),
    path('creer_production/', views.creer_production, name='creer_production'),
    path('productions/<int:production_id>/', views.detail_production, name='detail_production'),
]

