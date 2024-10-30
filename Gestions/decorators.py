from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def membre_required(view_func):
    """
    Ce décorateur vérifie si l'utilisateur est un membre avant d'autoriser l'accès à la vue.
    """
    @login_required  # L'utilisateur doit être connecté
    def wrapper(request, *args, **kwargs):
        if not request.user.is_membre:
            return redirect('accueil')  # Rediriger vers une page d'accueil ou autre si l'utilisateur n'est pas membre
        return view_func(request, *args, **kwargs)
    return wrapper
