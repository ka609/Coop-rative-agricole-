from django.shortcuts import render, get_object_or_404, redirect
from .models import Membre
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from productions.models import ProduitAgricole
from formations.models import Formation
from .forms import ThreadForm, ReplyForm
from .models import Thread,Reply
from .models import Profile
from django.urls import reverse



def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'liste_membres.html', {'membres': membres})

def detail_membre(request, id):
    membre = get_object_or_404(Membre, id=id)
    return render(request, 'detail_membre.html', {'membre': membre})

def index(request):
    return render(request, 'index.html')

# Correction de la vue d'inscription
def register(request):
    if request.method == "POST":
        username = request.POST['username']  # Assurez-vous que c'est 'username'
        firstname = request.POST['firstname']  # Assurez-vous que c'est 'firstname'
        lastname = request.POST['lastname']  # Assurez-vous que c'est 'lastname'
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']  # Assurez-vous que c'est 'password1'

        if password != password1:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'register.html')

        mon_utilisateur = User.objects.create_user(username=username, email=email, password=password)
        mon_utilisateur.first_name = firstname
        mon_utilisateur.last_name = lastname
        mon_utilisateur.save()

        messages.success(request, 'Votre compte a été créé avec succès.')
        return redirect('membres:login')  # Redirection vers la page de connexion après l'inscription

    return render(request, 'register.html')

# Renommer la vue pour éviter les conflits avec la fonction login de Django
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']  # Assurez-vous que c'est 'username'
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Renommez 'login' en 'auth_login' pour éviter les conflits
            firstname = user.first_name
            return redirect('membres:dashboard')
        else:
            messages.error(request, 'Mauvaise authentification')
            return redirect('membres:login')  # Assurez-vous que le nom correspond
    return render(request, 'login.html')

# Vue pour déconnexion
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Vous êtes déconnecté avec succès.')
    return redirect('membres:login')


def tableau_de_bord(request):
    utilisateur = request.user
    profile, created = Profile.objects.get_or_create(user=utilisateur)
    produits = ProduitAgricole.objects.all()  # Récupérer tous les produits agricoles
    formations = Formation.objects.all()  # Récupérer toutes les formations
    return render(request, 'tableau_de_bord.html', {
        'utilisateur': utilisateur,
        'profile': profile,
        'produits': produits,
        'formations': formations,
    })

def payer_produit(request):
    if request.method == "POST":
        produit_id = request.POST['produit']
        moyen_paiement = request.POST['moyen_paiement']
        # Logique de traitement du paiement ici
        # Vous pouvez rediriger vers une page de succès ou retourner à votre tableau de bord
        return redirect('membres:tableau_de_bord')  # Redirige vers le tableau de bord après le paiement
    else:
        # Récupérer tous les produits pour les afficher dans le formulaire
        produits = ProduitAgricole.objects.all()
        return render(request, 'payer_produit.html', {
            'produits': produits,
        })

def dashboard(request):
    return render(request, 'dashboard.html')

def create_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.author = request.user  # Associe l'auteur au thread
            thread.save()
            return redirect('forum')  # Redirige vers la page du forum
    else:
        form = ThreadForm()

    return render(request, 'create_thread.html', {'form': form})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    replies = thread.replies.all()  # Récupère toutes les réponses pour ce thread

    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.thread = thread
            reply.author = request.user
            reply.save()
            return redirect('thread_detail', thread_id=thread.id)
    else:
        reply_form = ReplyForm()

    return render(request, 'thread_detail.html', {
        'thread': thread,
        'replies': replies,
        'reply_form': reply_form
    })

def forum(request):
    threads = Thread.objects.all()  # Utilisation du modèle Thread
    return render(request, 'forum.html', {'threads': threads})

# Vue pour supprimer un thread
def supprimer_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)

    if request.user == thread.author:
        thread.delete()
        return redirect(reverse('membres:forum'))  # Redirection vers la page du forum
    else:
        # Si l'utilisateur n'est pas l'auteur, on peut afficher un message d'erreur ou rediriger.
        return redirect(reverse('membres:forum'))

    # Vue pour modifier un thread
def modifier_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)

    # Vérifie si l'utilisateur est l'auteur du thread
    if request.user != thread.author:
        return redirect('membres:forum')

    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('membres:thread_detail', thread_id=thread.id)
    else:
        form = ThreadForm(instance=thread)

    # Si la requête est GET, on affiche le formulaire avec les données actuelles
    return render(request, 'modifier_thread.html', {'form': form, 'thread': thread})

def contact_view(request):
    return render(request, 'contact.html')

def terms_view(request):
    return render(request, 'terms.html')