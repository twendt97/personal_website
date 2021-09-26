from app.thilos_website.settings.dev import SECRET_KEY
from .base import *
import os

DEBUG = False

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

try:
    from .local import *
except ImportError:
    pass
