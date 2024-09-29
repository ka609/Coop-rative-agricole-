from django.db import models
from membres.models import Membre

class Formateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    membres_participants = models.ManyToManyField(Membre)

class Progression(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    progression = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

