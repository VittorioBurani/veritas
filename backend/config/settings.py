"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = ['*']


# Deployment related defines:
DEVELOPMENT = 'DEVELOPMENT'
STAGING = 'STAGING'
PRODUCTION = 'PRODUCTION'
DEPLOYMENT_STAGE = os.environ.get('DEPLOYMENT_STAGE')

# IP, PORT and URL related defines:
PRIVATE_SERVER_IP = os.environ.get('PRIVATE_SERVER_IP')
HTTP_PORT = os.environ.get('HTTP_PORT')
HTTPS_PORT = os.environ.get('HTTPS_PORT')
BASE_URL = f'http://{PRIVATE_SERVER_IP}:{HTTP_PORT}'
BASE_URL_SECURE = f'https://{PRIVATE_SERVER_IP}:{HTTPS_PORT}'
DOMAIN_NAME = os.environ.get('DOMAIN_NAME')
DOMAIN_URL = f'http://{DOMAIN_NAME}'
DOMAIN_URL_SECURE = f'https://{DOMAIN_NAME}'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Rest Framework + module apps:
    'rest_framework',
    'corsheaders',
    'drf_spectacular',
    'django_filters',
    'rest_framework_simplejwt',
    # Custom apps:
    'custom',
    'accounts',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Custom Context Processors Here:
                'custom.context_processors.server_descriptors',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# CSRF Cookie For Reverse Proxy:
CSRF_COOKIE_SAMESITE = None
CSRF_COOKIE_HTTPONLY = False
CSRF_TRUSTED_ORIGINS = [
    f"http://localhost:{HTTP_PORT}",
    BASE_URL,
    BASE_URL_SECURE,
    DOMAIN_URL,
    DOMAIN_URL_SECURE,
]

# Django CORS Headers:
CORS_ALLOW_ALL_ORIGINS = True
CORS_URLS_REGEX = r"^/api/.*$"
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
CORS_EXPOSE_HEADERS = (
    'content-type',
    'X-CSRFToken',
    'X-Requested-With',
)
CORS_ALLOW_CREDENTIALS = True


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "db",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USERNAME"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "PORT": 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
    # Self defined: https://medium.com/geekculture/django-shorts-password-validators-95285c0936de
    {
        'NAME': 'custom.password_validators.NumberValidator',
    },
    {
        'NAME': 'custom.password_validators.UppercaseValidator',
    },
    {
        'NAME': 'custom.password_validators.SymbolValidator',
    },
]


AUTH_USER_MODEL = 'accounts.CustomUser'
AUTHENTICATION_BACKENDS = [
    # 'django.contrib.auth.backends.ModelBackend',
    'accounts.model_backends.UserEmailBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static-serve'
STATIC_URL = 'static/'

MEDIA_ROOT = BASE_DIR / 'media-serve'
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Rest Framework Settings:
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication', # SIMPLE JWT Stateless
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # Django Filters for backend filtering:
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # DRF Spectacular -> OpenAPI Docs:
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


# DRF Spectacular -> OpenAPI Docs:
SPECTACULAR_SETTINGS = {
    'SERVE_INCLUDE_SCHEMA': True,
    'TITLE': f'OpenAPI Schema for {DOMAIN_NAME} Rest API',
    'DESCRIPTION': f'OpenAPI Schema for {DOMAIN_NAME} Rest API. This is not for public use. Use this schema for endpoint testing in DEBUG mode.',
    'VERSION': os.environ.get('VERSION'),
    'SERVERS': [
        {
            'url': f'http://localhost:{HTTP_PORT}',
            'description': 'Development'
        },
        {
            'url': DOMAIN_URL_SECURE,
            'description': 'Production'
        }
    ],
    'COMPONENT_SPLIT_REQUEST': True,
}


# SIMPLE JWT Settings:
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "RS256",
    "SIGNING_KEY": open(BASE_DIR / PRIVATE_KEY, 'rb').read(),
    "VERIFYING_KEY": open(BASE_DIR / PUBLIC_KEY, 'rb').read(),
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "TOKEN_OBTAIN_SERIALIZER": "accounts.api.serializers.CustomTokenObtainPairSerializer",
}
