from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Membre
from .models import Thread, Reply

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Membre
        fields = ['nom', 'prenom', 'email', 'telephone', 'photo_de_profil', 'password1', 'password2']


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
