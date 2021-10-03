from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '07*9o4h4lt6ov5bu^be%)^k#fi9dec4tcy!7)%_75#p9=o_yiv'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

# env = os.environ.copy()
# SECRET_KEY = env['SECRET_KEY']
# # 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# # For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
# ALLOWED_HOSTS = env['DJANGO_ALLOWED_HOSTS'].split(" ")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1'
]

try:
    from .local import *
except ImportError:
    pass
