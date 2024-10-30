from django.contrib import admin
from .models import Membre, Production, Produit, Commande, Formation, Tutoriel, Quiz, Question, Reponse, InscriptionFormation

# Admin pour le modèle Membre
@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ['prenom', 'nom', 'email', 'telephone', 'role']
    search_fields = ['prenom', 'nom', 'email']
    list_filter = ['role']

# Admin pour le modèle Production
@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ['membre', 'type_culture', 'date_plantation', 'etat_actuel']
    search_fields = ['type_culture', 'membre__nom']
    list_filter = ['etat_actuel']

# Admin pour le modèle Produit
@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'membre', 'prix', 'stock','photo']
    search_fields = ['nom', 'membre__nom']
    list_filter = ['prix']

# Admin pour le modèle Commande
@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['acheteur', 'produit', 'quantite', 'status']
    list_filter = ['status']
    search_fields = ['acheteur__nom', 'produit__nom']

# Admin pour le modèle Formation
@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ['titre', 'formateur', 'date_debut', 'date_fin']
    search_fields = ['titre', 'formateur__nom']

# Admin pour le modèle Tutoriel
@admin.register(Tutoriel)
class TutorielAdmin(admin.ModelAdmin):
    list_display = ['titre', 'formation']
    search_fields = ['titre', 'formation__titre']

# Admin pour le modèle Quiz
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['titre', 'formation']
    search_fields = ['titre', 'formation__titre']

# Admin pour le modèle Question
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'texte_question']
    search_fields = ['texte_question']

# Admin pour le modèle Réponse
@admin.register(Reponse)
class ReponseAdmin(admin.ModelAdmin):
    list_display = ['question', 'texte_reponse', 'correcte']
    list_filter = ['correcte']

# Admin pour le modèle InscriptionFormation
@admin.register(InscriptionFormation)
class InscriptionFormationAdmin(admin.ModelAdmin):
    list_display = ['membre', 'formation', 'progression', 'score_quiz']
    search_fields = ['membre__nom', 'formation__titre']
