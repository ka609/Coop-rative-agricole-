
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

class Production(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE, related_name="productions")
    type_culture = models.CharField(max_length=100)
    date_plantation = models.DateField()
    date_recolte_prevue = models.DateField()
    etat_actuel = models.CharField(max_length=100, choices=[('semis', 'Semis'), ('croissance', 'Croissance'), ('recolte', 'Récolte')])

    def __str__(self):
        return f"{self.type_culture} - {self.membre.prenom} {self.membre.nom}"


class Produit(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='produits/', blank=True, null=True)  # Champ pour l'image

    def __str__(self):
        return self.nom

class Commande(models.Model):
    acheteur = models.ForeignKey(Membre, on_delete=models.CASCADE, related_name="commandes")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    date_commande = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('en_cours', 'En cours'), ('livrée', 'Livrée'), ('annulée', 'Annulée')])

    def __str__(self):
        return f"Commande de {self.quantite} {self.produit.nom} par {self.acheteur.prenom} {self.membre.nom}"

# models.py (App: Formation)

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    formateur = models.CharField(max_length=100)

    def __str__(self):
        return self.titre

class Tutoriel(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name="tutoriels")
    titre = models.CharField(max_length=200)
    contenu = models.TextField()  # Peut contenir un texte ou un lien vers une vidéo
    fichier_video = models.FileField(upload_to="videos/", blank=True, null=True)  # Pour stocker les vidéos
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} (Formation: {self.formation.titre})"

class Quiz(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name="quizzes")
    titre = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.titre} (Formation: {self.formation.titre})"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    texte_question = models.TextField()

    def __str__(self):
        return self.texte_question

class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="reponses")
    texte_reponse = models.CharField(max_length=200)
    correcte = models.BooleanField(default=False)  # Indique si la réponse est correcte

    def __str__(self):
        return f"{self.texte_reponse} (Correcte: {self.correcte})"

class InscriptionFormation(models.Model):
    membre = models.ForeignKey("Gestions.Membre", on_delete=models.CASCADE, related_name="inscriptions")
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name="inscriptions")
    date_inscription = models.DateTimeField(auto_now_add=True)
    progression = models.FloatField(default=0.0)  # Suivi de la progression en pourcentage
    score_quiz = models.FloatField(default=0.0)  # Score obtenu aux quiz

    def __str__(self):
        return f"{self.membre.prenom} {self.membre.nom} (Progression: {self.progression}%, Score: {self.score_quiz})"

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
