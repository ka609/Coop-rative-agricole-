from django.shortcuts import render, get_object_or_404
from .models import Commande, Panier, Transaction

def liste_commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'commandes/liste_commandes.html', {'commandes': commandes})

def detail_commande(request, id):
    commande = get_object_or_404(Commande, id=id)
    return render(request, 'commandes/detail_commande.html', {'commande': commande})

def detail_panier(request):
    panier = get_object_or_404(Panier, membre=request.user)
    return render(request, 'commandes/detail_panier.html', {'panier': panier})

def liste_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'commandes/liste_transactions.html', {'transactions': transactions})

