from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import tableau_de_bord,payer_produit,index,dashboard,forum,create_thread, thread_detail,supprimer_thread,modifier_thread,contact_view,terms_view


app_name = 'membres_productions'

urlpatterns = [
    path('', views.liste_membres, name='liste_membres'),
    path('', index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:id>/', views.detail_membre, name='detail_membre'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tableau-de-bord/', tableau_de_bord, name='tableau_de_bord'),
    path('create/', create_thread, name='create_thread'),
    path('thread/<int:thread_id>/', thread_detail, name='thread_detail'),
    path('supprimer/<int:thread_id>/', views.supprimer_thread, name='supprimer_thread'),
    path('modifier/<int:thread_id>/', views.modifier_thread, name='modifier_thread'),
    path('forum/', views.forum, name='forum'),
   path('contact/', views.contact_view, name='contact'),
    path('terms/', views.terms_view, name='terms'),
    path('payer/', payer_produit, name='payer_produit'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

]
