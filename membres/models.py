from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Membre(AbstractUser):
    # Champs supplémentaires
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True)
    date_inscription = models.DateTimeField(auto_now_add=True)

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
