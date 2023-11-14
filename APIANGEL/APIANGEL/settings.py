import os
from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

AUTHENTICATION_BACKENDS = (
)

SECRET_KEY = 'django-insecure-+0+_+b^tkbjpyo$@i)*u5hz!y0)5taofw##n3)b&j0fo6-7$=7'

DEBUG = False

ALLOWED_HOSTS = ['*']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)




INSTALLED_APPS = [
    'api',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'APIANGEL.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

GOOGLE_MAPS_API_KEY = 'AIzaSyCpndRG8hcPLpCUGqWqkAuXI6B0CsJCsb4'

WSGI_APPLICATION = 'APIANGEL.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': 'localhost',
#         'PORT': 5432,
#         'NAME': 'NSOS_mexico',
#         'USER': 'postgres',
#         'PASSWORD': '12345',
#     }
# }






AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




STATIC_URL = '/static/'

#

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Configuración de correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Servidor SMTP de Gmail
EMAIL_PORT = 587  # Puerto de Gmail para TLS/STARTTLS
EMAIL_USE_TLS = True  # Usar TLS para conexión segura

# Credenciales de correo electrónico de Gmail
EMAIL_HOST_USER = 'angel585244102@gmail.com'  # Tu dirección de correo de Gmail
EMAIL_HOST_PASSWORD = 'jgfmvwqfyqgvnexu'  # Contraseña de tu cuenta de Gmail

# Configuración adicional para Gmail
# DEFAULT_FROM_EMAIL = 'angel585244102@gmail.com'  # Dirección predeterminada para enviar correos
# Asegúrate de habilitar "Acceso de aplicaciones menos seguras" en tu cuenta de Gmail
# Si deseas usar OAuth 2.0 para autenticación, hay que configurarla de forma diferente

