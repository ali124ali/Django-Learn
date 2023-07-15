from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

X_FRAME_OPTIONS = 'SAMEORIGIN'

ALLOWED_HOSTS = ['ali-dehkhodaei.ir', 'www.ali-dehkhodaei.ir']

# INSTALLED_APPS = []

# sites framework
SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'alidehkh_mydb',
		'USER': 'alidehkh_ali',
		'PASSWORD': '6rTQMGGCmceVTK9',
		'HOST':'localhost',
		'PORT':'3306',
	}
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

CSRF_COOKIE_SECURE = True

# django_compressor
COMPRESS_ENABLED = True

COMPRESS_URL = STATIC_URL

COMPRESS_ROOT = STATIC_ROOT

COMPRESS_OUTPUT_DIR = 'CACHE'

COMPRESS_FILTERS = {
    'css': ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.rCSSMinFilter'],
    'js': ['compressor.filters.jsmin.rJSMinFilter']
    }

COMPRESS_CSS_HASHING_METHOD = 'mtime'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)