"""
WSGI config for jooble_devops_school project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# If WEBSITE_HOSTNAME is defined as an environment variable, then we're running
# on Azure App Service and should use the production settings in production.py.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jooble_devops_school.settings')

application = get_wsgi_application()