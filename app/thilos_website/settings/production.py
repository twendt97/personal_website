from .base import *
import os

DEBUG = True

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']
# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = env['DJANGO_ALLOWED_HOSTS'].split(" ")

COMPRESS_OFFLINE = True
LIBSASS_OUTPUT_STYLE = 'compressed'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

try:
    from .local import *
except ImportError:
    pass