from django.shortcuts import render, get_object_or_404
from .models import ProduitAgricole

def liste_productions(request):
    productions = ProduitAgricole.objects.all()
    return render(request, 'productions/liste_productions.html', {'productions': productions})

def detail_production(request, id):
    production = get_object_or_404(ProduitAgricole, id=id)
    return render(request, 'productions/detail_production.html', {'production': production})
