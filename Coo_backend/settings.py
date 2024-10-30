import os
from pathlib import Path
import dj_database_url
import environ

# Initialiser l'environnement
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()  # Charger les variables d'environnement depuis .env si disponible

# Dossier principal du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète sécurisée pour la production
SECRET_KEY = env('SECRET_KEY', default='unsafe-default-key')

# Mode debug pour le développement uniquement
DEBUG = env('DEBUG')

# Domaines autorisés (ajoutez votre domaine Heroku ici)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1', 'monapp.herokuapp.com'])

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Gestions.apps.GestionsConfig',
    'accounts.apps.AccountsConfig',
    'crispy_forms',
    'crispy_bootstrap4',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Coo_backend.urls'

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Coo_backend.wsgi.application'

# Configuration de la base de données PostgreSQL pour Heroku
DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL', default='postgres://postgres:projet2024@localhost:5432/postgres'),
        conn_max_age=600,
        ssl_require=True
    )
}

# Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Paramètres de localisation
LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Gestion des fichiers statiques
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Fichiers médias
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Paramètres de sécurité pour Heroku
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_SSL_REDIRECT = not DEBUG
X_FRAME_OPTIONS = 'DENY'

# Configuration de l'email via SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Paramètres des messages
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}

# Défaut pour le champ clé primaire
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
