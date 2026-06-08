# Django Settings Example

import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

TEMPLATES = [
    {
        "BACKEND":
        "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            os.path.join(BASE_DIR, "templates")
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI application

WSGI_APPLICATION = "technical_service_tracking.wsgi.application"

# Password validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
]

# Localization

LANGUAGE_CODE = "tr-TR"

TIME_ZONE = "Europe/Istanbul"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"

# Static files

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = "/static/"

# Secret key
# Never upload real secret keys to GitHub

SECRET_KEY = "YOUR_SECRET_KEY"
