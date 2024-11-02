from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Membre, Production, Produit, Commande, Formation, Tutoriel
from .forms import MembreForm, ProductionForm, ProduitForm, CommandeForm, FormationForm, TutorielForm
from .models import Discussion, Message
from django.contrib.auth.decorators import login_required
from .utils import time_since_posted
from django.contrib.auth.models import User
from django.http import JsonResponse
from .paydounia import PaydouniaAPI
from django.contrib import messages



# Vues pour les Membres
class MembreListView(ListView):
    model = Membre
    template_name = 'membre_list.html'


class MembreCreateView(CreateView):
    model = Membre
    form_class = MembreForm
    template_name = 'membre_create.html'
    success_url = reverse_lazy('membre_list')


class MembreUpdateView(UpdateView):
    model = Membre
    form_class = MembreForm
    template_name = 'membre_update.html'
    success_url = reverse_lazy('membre_list')


class MembreDetailView(DetailView):
    model = Membre
    template_name = 'membre_detail.html'


class MembreDeleteView(DeleteView):
    model = Membre
    template_name = 'membre_delete.html'
    success_url = reverse_lazy('membre_list')


# Vues pour les Productions
class ProductionListView(ListView):
    model = Production
    template_name = 'production_list.html'


class ProductionCreateView(CreateView):
    model = Production
    form_class = ProductionForm
    template_name = 'production_create.html'
    success_url = reverse_lazy('production_list')


class ProductionUpdateView(UpdateView):
    model = Production
    form_class = ProductionForm
    template_name = 'production_update.html'
    success_url = reverse_lazy('production_list')


class ProductionDetailView(DetailView):
    model = Production
    template_name = 'production_detail.html'


class ProductionDeleteView(DeleteView):
    model = Production
    template_name = 'production_delete.html'
    success_url = reverse_lazy('production_list')


# Vues pour les Produits
class ProduitListView(ListView):
    model = Produit
    template_name = 'produit_list.html'


class ProduitCreateView(CreateView):
    model = Produit
    form_class = ProduitForm
    template_name = 'produit_create.html'
    success_url = reverse_lazy('Gestions:produit_list')

def form_valid(self, form):
    form.instance.membre = self.request.user  # Associe le produit au membre connecté
    return super().form_valid(form)

class ProduitUpdateView(UpdateView):
    model = Produit
    form_class = ProduitForm
    template_name = 'produit_update.html'
    success_url = reverse_lazy('Gestions:produit_list')


class ProduitDetailView(DetailView):
    model = Produit
    template_name = 'produit_detail.html'


class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'produit_delete.html'
    success_url = reverse_lazy('Gestions:produit_list')


# Vues pour les Commandes
class CommandeListView(ListView):
    model = Commande
    template_name = 'commande_list.html'


class CommandeCreateView(CreateView):
    model = Commande
    form_class = CommandeForm
    template_name = 'commande_create.html'
    success_url = reverse_lazy('Gestions:commande_list')


class CommandeUpdateView(UpdateView):
    model = Commande
    form_class = CommandeForm
    template_name = 'commande_update.html'
    success_url = reverse_lazy('Gestions:commande_list')


class CommandeDetailView(DetailView):
    model = Commande
    template_name = 'commande_detail.html'


class CommandeDeleteView(DeleteView):
    model = Commande
    template_name = 'commande_delete.html'
    success_url = reverse_lazy('Gestions:commande_list')


# Vues pour les Formations
class FormationListView(ListView):
    model = Formation
    template_name = 'formation_list.html'


class FormationCreateView(CreateView):
    model = Formation
    form_class = FormationForm
    template_name = 'formation_create.html'
    success_url = reverse_lazy('Gestions:formation_list')

# Vue pour mettre à jour une formation
class FormationUpdateView(UpdateView):
    model = Formation
    form_class = FormationForm
    template_name = 'formation_update.html'
    success_url = reverse_lazy('Gestions:formation_list')

# Vue pour supprimer une formation
class FormationDeleteView(DeleteView):
    model = Formation
    template_name = 'formation_delete.html'
    success_url = reverse_lazy('Gestions:formation_list')

# Vue pour afficher le détail d'une formation
class FormationDetailView(DetailView):
    model = Formation
    template_name = 'formation_detail.html'

# Vues pour les Tutoriels
class TutorielListView(ListView):
    model = Tutoriel
    template_name = 'tutoriel_list.html'


class TutorielCreateView(CreateView):
    model = Tutoriel
    form_class = TutorielForm
    template_name = 'tutoriel_create.html'
    success_url = reverse_lazy('Gestions:tutoriel_list')

class TutorielUpdateView(UpdateView):
    model = Tutoriel
    form_class = TutorielForm
    template_name = 'tutoriel_update.html'
    success_url = reverse_lazy('Gestions:tutoriel_list')


class TutorielDetailView(DetailView):
    model = Tutoriel
    template_name = 'tutoriel_detail.html'


class TutorielDeleteView(DeleteView):
    model = Tutoriel
    template_name = 'tutoriel_delete.html'
    success_url = reverse_lazy('Gestions:tutoriel_list')

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
    # Vérifiez si l'utilisateur est authentifié
    if not request.user.is_authenticated:
        messages.error(request, "Vous devez être connecté pour accéder à votre tableau de bord.")
        return redirect('index')  # Redirection en cas d'absence d'authentification

    # Affichez les informations de l'utilisateur connecté sans rechercher dans un autre modèle
    return render(request, 'dashboard.html', {
        'user': request.user,
    })

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

# Dans Gestions/views.py
def create_invoice_view(request):
    # Instanciez l'API Paydounia avec le mode test activé (ou désactivé selon votre besoin)
    paydounia_api = PaydouniaAPI(test_mode=True)

    # Exemples de paramètres de la facture
    amount = 1000  # Montant de la facture
    currency = "XOF"  # Devise
    description = "Achat de produits agricoles"

    # Créez une facture en appelant l'API
    response_data = paydounia_api.create_invoice(amount, currency, description)

    # Vérifiez la réponse et renvoyez un JsonResponse avec les détails
    return JsonResponse(response_data)
