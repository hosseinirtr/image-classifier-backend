"""
WSGI config for image_rd project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from images import model_loader  # Import to ensure model loads on startup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_rd.settings')

application = get_wsgi_application()