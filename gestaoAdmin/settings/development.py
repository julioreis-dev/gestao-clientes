from gestaoAdmin.settings.settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'anything'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
