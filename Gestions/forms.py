from django import forms
from .models import Membre, Production, Produit, Commande, Formation, Tutoriel, Quiz, Question, Reponse, InscriptionFormation

# Formulaire pour le modèle Membre
class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['prenom', 'nom', 'email', 'telephone', 'adresse', 'role']

# Formulaire pour le modèle Production
class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ['type_culture', 'date_plantation', 'date_recolte_prevue', 'etat_actuel']

# Formulaire pour le modèle Produit (ajout d'un produit à vendre)
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'stock', 'photo','membre']  # Ajout du champ photo

# Formulaire pour le modèle Commande (achat d'un produit)
class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['acheteur', 'produit', 'quantite', 'status']  # Inclut tous les champs du modèle
        widgets = {
            'status': forms.Select(choices=[('en_cours', 'En cours'), ('livrée', 'Livrée'), ('annulée', 'Annulée')]),
        }

# Formulaire pour le modèle Formation
class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['titre', 'description', 'date_debut', 'date_fin', 'formateur']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Titre de la formation'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 4, 'placeholder': 'Description'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
            'formateur': forms.Select(attrs={'class': 'form-control mb-3'}),
        }

# Formulaire pour le modèle Tutoriel
class TutorielForm(forms.ModelForm):
    class Meta:
        model = Tutoriel
        fields = ['formation', 'titre', 'contenu', 'fichier_video']

# Formulaire pour le modèle Quiz
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['formation', 'titre', 'description']

# Formulaire pour le modèle Question
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quiz', 'texte_question']

# Formulaire pour le modèle Réponse
class ReponseForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ['question', 'texte_reponse', 'correcte']

# Formulaire pour Inscription à une formation
class InscriptionFormationForm(forms.ModelForm):
    class Meta:
        model = InscriptionFormation
        fields = ['formation']
