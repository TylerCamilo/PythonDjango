from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'empleado',
        'USER': 'camilo',
        'PASSWORD': 'camilocurso',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
