from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, UserForm
from django.contrib import messages

# Vue pour la connexion
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Connexion réussie !')
                return redirect('index')  # Rediriger vers la page d'accueil après connexion
            else:
                messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect.')
        else:
            messages.error(request, 'Erreur de validation du formulaire.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# Vue pour l'inscription
def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscription réussie. Vous pouvez maintenant vous connecter.')
            return redirect('accounts:login')  # Rediriger vers la page de connexion après inscription
        else:
            messages.error(request, 'Erreur lors de l’inscription. Veuillez corriger les erreurs ci-dessous.')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})


# Vue pour la déconnexion
def logout_view(request):
    logout(request)
    messages.info(request, 'Vous avez été déconnecté avec succès.')
    return redirect('accounts:login')  # Rediriger vers la page de connexion après déconnexion
