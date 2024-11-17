from pathlib import Path
import os
import dj_database_url
from decouple import config
import cloudinary.api

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète
SECRET_KEY = config('SECRET_KEY', default='your-default-secret-key')

# Mode Debug
DEBUG = config('DEBUG', default=False, cast=bool)


# Hôtes autorisés
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

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
    'cloudinary',  # Ajout de Cloudinary
    'cloudinary_storage',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Coo_backend.urls'

# Templates
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

# Base de données
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# Validation du mot de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalisation
LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Fichiers statiques et média
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#STORAGES = {
    # "default": {
        # "BACKEND": "django.core.files.storage.FileSystemStorage",
        # "OPTIONS": {
            #  "location": BASE_DIR / "media",
            # },
        # },
    #"staticfiles": {
        # "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        # },
#}

STORAGES = {
 'default': {
    'BACKEND': 'cloudinary_storage.storage.MediaCloudinaryStorage',
   },
  'staticfiles': {
         'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
  },
}

# Clé primaire par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuration de l'email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#les cookies
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_AGE = 3600  # 1 heure en secondes
SESSION_EXPIRE_AT_BROWSER_CLOSE =True



SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


CINETPAY_API_KEY = config("CINETPAY_API_KEY")
CINETPAY_SITE_ID = config("CINETPAY_SITE_ID")

# Configure Cloudinary en utilisant CLOUDINARY_URL depuis le fichier .env
cloudinary.config(
    cloud_name=config('CLOUDINARY_URL').split('@')[1],
    api_key=config('CLOUDINARY_URL').split('://')[1].split(':')[0],
    api_secret=config('CLOUDINARY_URL').split(':')[2].split('@')[0]
)