from django.db import models
from membres.models import Membre
from productions.models import ProduitAgricole

class Commande(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('payee', 'Payée'),
        ('livree', 'Livrée'),
    ]
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    produit = models.ForeignKey(ProduitAgricole, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='en_attente')
    date_commande = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Commande {self.id} par {self.membre.username}"

class Panier(models.Model):
    membre = models.OneToOneField(Membre, on_delete=models.CASCADE)
    produits = models.ManyToManyField(ProduitAgricole, through='PanierProduit')

class PanierProduit(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    produit = models.ForeignKey(ProduitAgricole, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

class Transaction(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    date_paiement = models.DateTimeField(auto_now_add=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f"Transaction {self.transaction_id} pour la commande {self.commande.id}"

