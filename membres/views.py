from django.shortcuts import render, get_object_or_404
from .models import Membre

def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'membres/liste_membres.html', {'membres': membres})

def detail_membre(request, id):
    membre = get_object_or_404(Membre, id=id)
    return render(request, 'membres/detail_membre.html', {'membre': membre})

