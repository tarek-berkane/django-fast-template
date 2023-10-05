from base import *


SECRET_KEY = "django-insecure-u%)am6-!hq)h7%wdfhh@^%ie&8gaqi4#w^@-@12_hd%a4q@2ly"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    "django_browser_reload",
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]


# =======================
# DATABASE
# =======================
{%- if  cookiecutter.use_sqlite3_for_dev == True or cookiecutter.project_database == "sqlite3"  -%}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
{%- elif cookiecutter.project_database == "postgresql" -%}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {
            "service": "my_service",
            "passfile": ".my_pgpass",
        },
    }
}
{% endif %}

{%- if  cookiecutter.include_log  -%}
# =======================
# LOGGING
# =======================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}
{% endif %}


{%- if  cookiecutter.include_redis  -%}
# =======================
# REDIS
# =======================
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
{% endif %}


{%- if  cookiecutter.include_redis  -%}
# =======================
# EMAIL
# =======================
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
{% endif %}