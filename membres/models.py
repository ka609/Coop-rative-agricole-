from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User

class Membre(AbstractUser):
    # Champs supplémentaires
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True)
    date_inscription = models.DateTimeField(auto_now_add=True)
    photo_de_profil = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name="Photo de profil")

    # Rôle
    ROLE_CHOICES = [
        ('membre', 'Membre'),
        ('admin', 'Administrateur'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='membre')

    # Méthodes de rôle
    def est_administrateur(self):
        return self.role == 'admin'

    def est_membre(self):
        return self.role == 'membre'

    # Redéfinition du champ de nom complet pour AbstractUser
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'username']

    # Champs liés aux groupes et permissions
    groups = models.ManyToManyField(
        Group,
        related_name='membres_custom',  # Changement de related_name pour éviter le conflit
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='membres_custom',  # Changement de related_name pour éviter le conflit
        blank=True,
    )

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.role}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Lien avec le modèle utilisateur
    bio = models.TextField(blank=True)
    # Ajoutez d'autres champs si nécessaire

    def __str__(self):
        return self.user.username

class Thread(models.Model):
        title = models.CharField(max_length=255)
        content = models.TextField()
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title

class Reply(models.Model):
        thread = models.ForeignKey(Thread, related_name='replies', on_delete=models.CASCADE)
        content = models.TextField()
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f'Reply by {self.author} on {self.thread}'