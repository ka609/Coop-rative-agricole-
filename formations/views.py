from django.shortcuts import render, get_object_or_404
from .models import Formation

# Vue pour la liste des formations
def liste_formations(request):
    formations = Formation.objects.all()
    return render(request, 'formations/liste_formations.html', {'formations': formations})

# Vue pour les détails d'une formation
def detail_formation(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id)
    return render(request, 'formations/detail_formation.html', {'formation': formation})

# Vue pour prendre un quiz (QIZ)
def prendre_quiz(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id, type_formation='QIZ')
    if request.method == 'POST':
        reponse = request.POST.get('reponse')
        est_correct = (reponse == formation.bonne_reponse)
        return render(request, 'formations/resultat_quiz.html', {
            'formation': formation,
            'est_correct': est_correct,
        })
    return render(request, 'formations/quiz.html', {'formation': formation})
