import os
import environ
from base import *

config_file = "<SET-PATH-HERE>"
env = environ.Env()
environ.Env.read_env(os.path.join(config_file, ".env"))

SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# =======================
# DATABASE
# =======================

{%- if cookiecutter.project_database == "sqlite3"  -%}
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
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "log/output.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": True,
        },
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
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
{% endif %}