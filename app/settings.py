import django_heroku
from pathlib import Path
import os
import environ

from django.utils.translation import ugettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

IS_ON_HEROKU = env.bool('ON_HEROKU', default=False)

if not IS_ON_HEROKU:
    env.read_env(os.path.join(BASE_DIR,'.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.get_value('DEBUG', cast = bool)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['portfolio-5616.herokuapp.com']

PROJECT_NAME = os.path.basename(BASE_DIR)
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-*r(vg%+-fo_ho+bowl(rhtg87rtzekun30o%v(6c&6j403z_s='


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'app.urls' #プロジェクト名をxxxに入れる

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'app.wsgi.application' #プロジェクト名をxxxに入れる


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
    

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

# 英語対応の場合は 下記コメントアウトを外す
LANGUAGES = [
    ('ja', _('日本語')),
    # ('en', _('English')),
]

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and Media files
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'


# Upload Settings

DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000
FILE_UPLOAD_MAX_MEMORY_SIZE = 15728640
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640


django_heroku.settings(locals())