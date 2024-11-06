
# models.py (App: Gestion)
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Membre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, unique=True)
    adresse = models.TextField()
    date_inscription = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=50, choices=[('agriculteur', 'Agriculteur'), ('partenaire', 'Partenaire'), ('administrateur', 'Administrateur')])

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class ProductionAgricole(models.Model):
    culture = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    superficie = models.FloatField()
    rendement = models.FloatField()
    date_plantation = models.DateField()
    date_recolte = models.DateField()
    commentaires = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.culture} - {self.region}"

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='videos_formations/', null=True, blank=True)  # Tutoriel vidéo
    quiz = models.TextField(help_text="Ajoutez des questions de quiz pour autoformation", null=True, blank=True)
    date_creation = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey(Membre, on_delete=models.SET_NULL, null=True, blank=True, related_name="formations")

    def __str__(self):
        return self.titre

class Discussion(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussions')

    def __str__(self):
        return self.title

class Message(models.Model):
    discussion = models.ForeignKey(Discussion, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)  # Pour les réponses aux messages

    def __str__(self):
        return f'{self.created_by.username}: {self.content[:20]}'

class Article(models.Model):
    vendeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles_vendus")
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos_articles/', blank=True, null=True)
    date_publication = models.DateTimeField(default=timezone.now)
    notification_envoyee = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

    def peut_etre_commande_par(self, utilisateur):
        """Vérifie si l'utilisateur connecté peut commander cet article."""
        return self.vendeur != utilisateur

class Transaction(models.Model):
    acheteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="achats")
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, default="en attente")

    def __str__(self):
        return f"Transaction {self.id} pour {self.article.nom}"
