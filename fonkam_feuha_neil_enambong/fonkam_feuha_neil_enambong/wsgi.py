"""
WSGI config for fonkam_feuha_neil_enambong project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fonkam_feuha_neil_enambong.settings')

application = get_wsgi_application()
