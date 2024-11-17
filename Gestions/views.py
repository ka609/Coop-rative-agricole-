from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Membre, ProductionAgricole, Formation,Transaction,Article
from .forms import MembreForm,ArticleForm, FormationForm,ProductionAgricoleForm
from .models import Discussion, Message
from django.contrib.auth.decorators import login_required
from .utils import time_since_posted
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse, HttpResponseBadRequest
import csv, io
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
import base64
import matplotlib.pyplot as plt
from cinetpay_sdk.s_d_k import Cinetpay
from decouple import config


# Charger les clés API et l'ID du site à partir des variables d'environnement
API_KEY = config('CINETPAY_API_KEY')
SITE_ID = config('CINETPAY_SITE_ID')

def initiate_payment(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        amount = request.POST.get('amount')

        # Validation des données
        if not all([name, surname, amount]):
            return HttpResponseBadRequest("Tous les champs sont requis.")

        try:
            # Conversion du montant en nombre
            amount = float(amount)
        except ValueError:
            return HttpResponseBadRequest("Le montant doit être un nombre valide.")

        # Générer un ID unique pour la transaction
        transaction_id = f"TRX-{name[:3].upper()}-{surname[:3].upper()}-{str(abs(hash(name + surname)))[:8]}"

        # Préparer les données pour CinetPay
        data = {
            'amount': amount,
            'currency': "XOF",
            'transaction_id': transaction_id,
            'description': f"Paiement de {name} {surname} pour un montant de {amount} XOF",
            'return_url': 'http://http://127.0.0.1:8000/Gestions/success/',
            'notify_url': 'http://http://127.0.0.1:8000/Gestions/notify/',
            'customer_name': name,
            'customer_surname': surname,
        }

    try:
        # Initialiser le client CinetPay
        client = Cinetpay(API_KEY, SITE_ID)

        # Initialiser le paiement
        response = client.PaymentInitialization(data)

        # Vérifier la réponse
        if response.get('code') == '201':  # Code 201 signifie "CREATED"
            # Extraire l'URL de paiement
            payment_url = response['data']['payment_url']
            # Rediriger vers l'URL de paiement
            return redirect(payment_url)
        else:
            # Afficher un message d'erreur
            return render(request, 'error.html',
                          {'message': response.get('message', 'Erreur lors de l\'initialisation du paiement.')})

    except Exception as e:
        # Gérer les erreurs
        return render(request, 'error.html', {'message': f"Erreur interne : {str(e)}"})

        # Rediriger vers la page d'accueil si ce n'est pas une requête POST
    return redirect('Gestions:dashboard')

def success(request):
    """Vue pour un paiement réussi"""
    return render(request, 'success.html', {'message': "Paiement réussi !"})


def error(request):
    """Vue pour une erreur"""
    return render(request, 'error.html', {'message': "Une erreur est survenue."})


# Vues pour les Membres
class MembreListView(ListView):
    model = Membre
    template_name = 'membre_list.html'


class MembreCreateView(CreateView):
    model = Membre
    form_class = MembreForm
    template_name = 'membre_create.html'
    success_url = reverse_lazy('Gestions:membre_list')


class MembreUpdateView(UpdateView):
    model = Membre
    form_class = MembreForm
    template_name = 'membre_update.html'
    success_url = reverse_lazy('Gestions:membre_list')


class MembreDetailView(DetailView):
    model = Membre
    template_name = 'membre_detail.html'


class MembreDeleteView(DeleteView):
    model = Membre
    template_name = 'membre_delete.html'
    success_url = reverse_lazy('Gestions:membre_list')

def suivi_agricole(request):
    productions = ProductionAgricole.objects.all()
    return render(request, 'suivi_agricole.html', {'productions': productions})


def liste_formations(request):
    # Récupération de toutes les formations
    formations = Formation.objects.all()

    # Paramètre de recherche
    query = request.GET.get('q', '')
    if query:
        formations = formations.filter(titre__icontains=query)  # Recherche insensible à la casse

    # Pagination
    paginator = Paginator(formations, 6)  # Afficher 6 formations par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Rendu de la page avec les données paginées et de recherche
    return render(request, 'liste_formations.html', {'page_obj': page_obj, 'query': query})

def detail_formation(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id)
    return render(request, 'detail_formation.html', {'formation': formation})

def creer_formation(request):
    if request.method == 'POST':
        form = FormationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Gestions:liste_formations')  # Redirection vers la liste des formations
    else:
        form = FormationForm()
    return render(request, 'creer_formation.html', {'form': form})

def supp_formation(request, id):
    formation = get_object_or_404(Formation, id=id)
    formation.delete()
    return redirect('Gestions:liste_formations')

def form_valid(self, form):
    form.instance.membre = self.request.user  # Associe le produit au membre connecté
    return super().form_valid(form)

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def support(request):
    return render(request, 'support.html')

def legal(request):
    return render(request, 'legal.html')

def index(request):
    return render(request, 'index.html')


def dashboard(request):
    articles = Article.objects.all()  # Récupère tous les articles
    total_users = User.objects.count()  # Compte tous les utilisateurs
    total_members = Membre.objects.count()  # Compte seulement les membres enregistrés
    total_formations = Formation.objects.count()  # Compte le nombre de formations
    formations = Formation.objects.all()

    context = {
        'articles': articles,
        'user': request.user,  # Utilisateur actuel
        'total_users': total_users,  # Nombre total d'utilisateurs
        'total_members': total_members,  # Nombre total de membres
        'total_formations': total_formations,  # Nombre total de formations
        'formations': formations,
    }

    return render(request, 'dashboard.html', context)

@login_required
def send_message(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            message = Message.objects.create(
                content=content,
                created_by=request.user,
                discussion=discussion
            )
            message.time_since = time_since_posted(message.created_at)  # Calcul de la date relative
        return redirect('Gestions:discussion_detail', discussion_id=discussion.id)

    messages = Message.objects.filter(discussion=discussion).order_by('-created_at')
    # Applique la fonction de formatage de la date à chaque message
    for message in messages:
        message.time_since = time_since_posted(message.created_at)

    return render(request, 'send_message.html', {'discussion': discussion, 'messages': messages})

@login_required
def edit_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    # Vérification si l'utilisateur est l'auteur du message
    if request.user != message.created_by:
        return redirect('Gestions:discussion_detail', discussion_id=message.discussion.id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            message.content = content
            message.save()
        return redirect('Gestions:discussion_detail', discussion_id=message.discussion.id)

    message.time_since = time_since_posted(message.created_at)  # Calcul de la date relative
    return render(request, 'edit_message.html', {'message': message})


@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    # Vérification si l'utilisateur est l'auteur du message
    if request.user == message.created_by:
        discussion_id = message.discussion.id
        message.delete()
        return redirect('Gestions:discussion_detail', discussion_id=discussion_id)

    return redirect('Gestions:discussion_detail', discussion_id=message.discussion.id)


@login_required
def reply_message(request, message_id):
    parent_message = get_object_or_404(Message, id=message_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            reply_message = Message.objects.create(
                content=content,
                created_by=request.user,
                discussion=parent_message.discussion,
                parent=parent_message
            )
            reply_message.time_since = time_since_posted(reply_message.created_at)  # Calcul de la date relative
        return redirect('Gestions:discussion_detail', discussion_id=parent_message.discussion.id)

    parent_message.time_since = time_since_posted(parent_message.created_at)  # Calcul de la date relative
    return render(request, 'reply_message.html', {'parent_message': parent_message})


@login_required
def discussion_detail(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    messages = Message.objects.filter(discussion=discussion).order_by('created_at')

    for message in messages:
        message.time_since = time_since_posted(message.created_at)  # Utilisation de utils.py

    return render(request, 'discussion_detail.html', {
        'discussion': discussion,
        'messages': messages
    })
@login_required
def forum(request):
    discussions = Discussion.objects.all().order_by('-created_at')
    total_messages = Message.objects.count()
    active_members = User.objects.filter(is_active=True).count()

    context = {
        'discussions': discussions,
        'total_messages': total_messages,
        'active_members': active_members,
    }
    return render(request, 'forum.html', context)

@login_required
def create_discussion(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            discussion = Discussion.objects.create(
                title=title,
                created_by=request.user
            )
            # Création du premier message associé à la discussion
            Message.objects.create(
                content=content,
                created_by=request.user,
                discussion=discussion
            )
            return redirect('Gestions:discussion_detail', discussion_id=discussion.id)

    return render(request, 'create_discussion.html')

def liste_articles(request):
    articles = Article.objects.all()  # Utilisez un 'a' minuscule pour 'articles'
    return render(request, 'liste_articles.html', {'articles': articles})  # Utilisez 'articles' ici


@login_required
def publier_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.vendeur = request.user  # Attribuez l'utilisateur connecté comme vendeur
            article.save()
            return redirect('Gestions:dashboard')  # Redirigez vers le tableau de bord
    else:
        form = ArticleForm()

    return render(request, 'publier_article.html', {'form': form})

def ecommerce(request):
    utilisateur = request.user
    query = request.GET.get('query', '')  # Récupérer la recherche, s'il y en a une
    articles = Article.objects.all().order_by('-date_publication')

    # Filtrer les articles par recherche
    if query:
        articles = articles.filter(
            Q(nom__icontains=query) | Q(description__icontains=query)
        )

    paginator = Paginator(articles, 8)  # 8 articles par page
    page_number = request.GET.get('page')
    articles_page = paginator.get_page(page_number)

    # Ajouter une propriété pour indiquer si chaque article peut être commandé
    articles_commande = [
        {
            'article': article,
            'peut_etre_commande': article.peut_etre_commande_par(utilisateur)
        }
        for article in articles_page
    ]

    # Notifications pour les nouveaux articles (non encore notifiés)
    notifications = Article.objects.filter(notification_envoyee=False)

    # Marquer les notifications comme envoyées après les avoir affichées
    for article in notifications:
        article.notification_envoyee = True
        article.save()

    context = {
        'articles_commande': articles_commande,
        'notifications': [f"Nouveau article publié : {article.nom}" for article in notifications],
        'utilisateur': utilisateur,
    }
    return render(request, 'ecommerce.html', context)


@login_required
def acheter_article(request, article_id):
    # Récupérer l'article et vérifier si l'utilisateur peut le commander
    article = get_object_or_404(Article, id=article_id)
    if not article.peut_etre_commande_par(request.user):
        return redirect('Gestions:ecommerce')  # Rediriger si l'utilisateur ne peut pas commander cet article

    # Créer une transaction (à adapter selon vos besoins)
    Transaction.objects.create(
        acheteur=request.user,
        article=article,
        montant=article.prix,
        statut="en attente"
    )
    # Rediriger ou afficher un message de confirmation
    return redirect('Gestions:ecommerce')


def detail_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # Vérifie si l'utilisateur peut commander cet article
    peut_commander = article.peut_etre_commande_par(request.user) if request.user.is_authenticated else False

    return render(request, 'detail_article.html', {
        'article': article,
        'peut_commander': peut_commander
    })


# views.py
def suivi_agricole(request):
    productions = ProductionAgricole.objects.all()
    commentaires = [prod.commentaires for prod in productions if prod.commentaires]

    # Graphiques et statistiques
    cultures = [p.culture for p in productions]
    rendements = [p.rendement for p in productions]

    # Graphique des rendements par culture
    plt.figure(figsize=(8, 5))
    plt.bar(cultures, rendements, color="green")
    plt.xlabel("Culture")
    plt.ylabel("Rendement (tonnes/ha)")
    plt.title("Rendements par culture")

    # Sauvegarder le graphique en mémoire
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphique_rendement = base64.b64encode(image_png).decode("utf-8")

    # Afficher la carte interactive du Burkina Faso (une image temporaire pour l'exemple)
    carte_url = "https://www.example.com/carte_burkina_faso.png"  # Remplacer par une carte interactive

    # Formulaire de création de production (en cas d'ajout)
    if request.method == 'POST':
        form = ProductionAgricoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Gestions:suivi_agricole')
    else:
        form = ProductionAgricoleForm()

    context = {
        'productions': productions,
        'commentaires': commentaires,
        'graphique_rendement': graphique_rendement,
        'carte_url': carte_url,
        'form': form,
    }
    return render(request, 'suivi_agricole.html', context)

@login_required
def supprimer_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    # Vérifie si l'utilisateur actuel est l'auteur de l'article
    if request.user == article.vendeur:
        article.delete()
        messages.success(request, "L'article a été supprimé avec succès.")
    else:
        messages.error(request, "Vous n'êtes pas autorisé à supprimer cet article.")

    # Redirige vers la page de la boutique ou la liste des articles
    return redirect('Gestions:ecommerce')


def detail_production(request, production_id):
    production = get_object_or_404(ProductionAgricole, id=production_id)
    return render(request, 'detail_production.html', {'production': production})

def telecharger_rapport_confirmation(request):
    return render(request, 'telecharger_rapport.html')

def telecharger_rapport_csv(request):
    # Récupération des données de production
    productions = ProductionAgricole.objects.all()

    # Préparation de la réponse CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rapport_productions.csv"'

    # Écriture dans le fichier CSV
    writer = csv.writer(response)
    writer.writerow(['Culture', 'Région', 'Superficie (ha)', 'Rendement (tonnes/ha)', 'Date de Plantation', 'Date de Récolte', 'Commentaires'])
    for production in productions:
        writer.writerow([
            production.culture,
            production.region,
            production.superficie,
            production.rendement,
            production.date_plantation,
            production.date_recolte,
            production.commentaires
        ])

    return response

def ajouter_commentaire(request):
    if request.method == 'POST':
        production_id = request.POST.get('production_id')

        # Vérifiez si production_id est fourni
        if not production_id:
            messages.error(request, "Aucun ID de production fourni.")
            return redirect('Gestions:suivi_agricole')

        try:
            production = get_object_or_404(ProductionAgricole, id=production_id)
            commentaire = request.POST.get('commentaire')
            production.commentaires = commentaire
            production.save()
            messages.success(request, "Commentaire ajouté avec succès.")
        except ProductionAgricole.DoesNotExist:
            messages.error(request, "Production introuvable.")

    return redirect('Gestions:suivi_agricole')

def creer_production(request):
    if request.method == 'POST':
        form = ProductionAgricoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Gestions:suivi_agricole')  # Redirection après succès
    else:
        form = ProductionAgricoleForm()
    return render(request, 'creer_production.html', {'form': form})

def payment_form(request):
    return render(request, 'payment_form.html')


def payment_success(request):
    # Logique à exécuter après un paiement réussi
    return render(request, 'success.html', {'message': "Paiement réussi. Merci pour votre transaction !"})

def payment_notify(request):
    # Logique à exécuter pour traiter les notifications de paiement de CinetPay
    if request.method == 'POST':
        # Extraire et traiter les données reçues
        data = request.POST
        print("Notification de CinetPay :", data)
        # Vous pouvez sauvegarder ou vérifier les données ici
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'invalid request'}, status=400)
