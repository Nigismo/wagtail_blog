from .base import *  # noqa
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# -- Recommended CodeRed Cloud settings ---------------------------------------

ALLOWED_HOSTS = ['nigismo.codered.cloud']

SECRET_KEY = os.environ["RANDOM_SECRET_KEY"]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Built-in email sending service provided by CodeRed Cloud.
# Change this to a different backend or SMTP server to use your own.
EMAIL_BACKEND = "django_sendmail_backend.backends.EmailBackend"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.environ["DB_HOST"],
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "OPTIONS": {"sslmode": "require"},
    }
}

WAGTAILADMIN_BASE_URL = f"http://{os.environ['VIRTUAL_HOST']}"
