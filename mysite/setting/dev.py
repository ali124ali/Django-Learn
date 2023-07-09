from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zobl^9t)ifpr1b%c1f3kqj9iy(l14mk9g*l=yp16p3ao5bb%c3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
X_FRAME_OPTIONS = 'SAMEORIGIN'

ALLOWED_HOSTS = []

# INSTALLED_APPS = []

# sites framework
SITE_ID = 3


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]