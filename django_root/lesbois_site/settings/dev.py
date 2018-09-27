import environ

env = environ.Env()
env.read_env('.env.dev')

from .base import *

ALLOWED_HOSTS += [
    'localhost'
] 

INSTALLED_APPS += []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
