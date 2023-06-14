"""
WSGI config for wagtail_bootstrap_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wagtail_bootstrap_blog.settings.prod")

application = get_wsgi_application()

# import os
# import sys
# #
# ## assuming your django settings file is at '/home/Nigismo/mysite/mysite/settings.py'
# ## and your manage.py is is at '/home/Nigismo/mysite/manage.py'
# path = '/home/Nigismo/wagtail_blog'
# if path not in sys.path:
#     sys.path.append(path)
# # /home/Nigismo/wagtail_blog/wagtail_bootstrap_blog/settings/production.py
# os.environ['DJANGO_SETTINGS_MODULE'] = 'wagtail_bootstrap_blog.settings.production'
# #
# ## then:
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
