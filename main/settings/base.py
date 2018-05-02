"""
Django settings for Portfolio project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from .env import env
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3w3_o3++mx^@lmyv9zv^1)85l=4#o8i@tphql-9e2*psy+$xc3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = env('ALLOWED_HOSTS', default=['*'])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webpack_loader',
    'compressor',
    'main',
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

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
            os.path.join(WEBSITE_ROOT, 'templates'),
            ],
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB', default='tattoo_db'),
        'USER': env('POSTGRES_USER', default='user_tattoo'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='random'),
        'HOST': env('POSTGRES_HOST', default='127.0.0.1'),
        'PORT': env('POSTGRES_PORT', default=5432),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(WEBSITE_ROOT, 'webpack.manifest.app.json'),
        'POLL_INTERVAL': 1,
    },
    'SPA': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(WEBSITE_ROOT, 'webpack.manifest.spa.json'),
        'POLL_INTERVAL': 1,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'main.compressor_filters.PatchedSCSSCompiler'),
)
if DEBUG:
    COMPRESS_CSS_FILTERS = (
        'main.compressor_filters.CustomCssAbsoluteFilter',
    )
else:
    COMPRESS_CSS_FILTERS = (
        'main.compressor_filters.CustomCssAbsoluteFilter',
        'django_compressor_autoprefixer.AutoprefixerFilter',
    )

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'compressor': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'compressor'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = env(
    'STATIC_ROOT',
    default=os.path.join(WEBSITE_ROOT, 'static/'))
#STATICFILES_DIRS = (
#    os.path.join(WEBSITE_ROOT, "static_root"),
#)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(WEBSITE_ROOT, 'media')