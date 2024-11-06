from django import forms
from .models import Membre,Article, Formation,ProductionAgricole

# Formulaire pour le modèle Membre
class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['prenom', 'nom', 'email', 'telephone', 'adresse', 'role']


class ProductionAgricoleForm(forms.ModelForm):
    class Meta:
        model = ProductionAgricole
        fields = ['culture', 'region', 'superficie', 'rendement', 'date_plantation', 'date_recolte', 'commentaires']
        widgets = {
            'culture': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'superficie': forms.NumberInput(attrs={'class': 'form-control'}),
            'rendement': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_plantation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_recolte': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'commentaires': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }


class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['titre', 'description', 'video', 'quiz', 'auteur']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nom', 'prix', 'description', 'photo']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }