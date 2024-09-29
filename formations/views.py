from django.shortcuts import render, get_object_or_404
from .models import Formation, Formateur, Categorie

def liste_formations(request):
    formations = Formation.objects.all()
    return render(request, 'formations/liste_formations.html', {'formations': formations})

def detail_formation(request, id):
    formation = get_object_or_404(Formation, id=id)
    return render(request, 'formations/detail_formation.html', {'formation': formation})

def liste_formateurs(request):
    formateurs = Formateur.objects.all()
    return render(request, 'formations/liste_formateurs.html', {'formateurs': formateurs})

def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'formations/liste_categories.html', {'categories': categories})

