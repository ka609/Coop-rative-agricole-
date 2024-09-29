from django.db import models

class ProduitAgricole(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    quantite_disponible = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

