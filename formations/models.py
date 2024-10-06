from django.db import models

class Formation(models.Model):
    TYPE_CHOICES = [
        ('QIZ', 'Quiz'),
        ('TUTORIAL', 'Tutoriel'),
        ('DOCUMENT', 'Document'),
        ('VIDEO', 'Vidéo'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    type_formation = models.CharField(max_length=10, choices=TYPE_CHOICES)
    fichier = models.FileField(upload_to='formations/', null=True, blank=True)  # Pour les documents et vidéos
    lien_video = models.URLField(null=True, blank=True)  # Pour les tutoriels vidéo
    date_publication = models.DateTimeField(auto_now_add=True)

    # Pour les QCM (QIZ)
    question = models.TextField(null=True, blank=True)  # Question du QIZ
    option_1 = models.CharField(max_length=200, null=True, blank=True)
    option_2 = models.CharField(max_length=200, null=True, blank=True)
    option_3 = models.CharField(max_length=200, null=True, blank=True)
    option_4 = models.CharField(max_length=200, null=True, blank=True)
    bonne_reponse = models.CharField(max_length=200, null=True, blank=True)  # Réponse correcte pour le QIZ

    def __str__(self):
        return self.titre
