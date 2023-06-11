from .base import *

DEBUG = False


ALLOWED_HOSTS = ['nigismo.pythonanywhere.com']

SECRET_KEY = "*kh&+u9^v^))bi2z3q*-=d0w_(s#vmgs_l8xgjk-4i5m78+e*)"

ROOT_URLCONF = "wagtail_bootstrap_blog.urls"


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
NOCAPTCHA = True
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]


try:
    from .local import *
except ImportError:
    pass
