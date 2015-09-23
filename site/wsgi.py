"""
WSGI config for ldbox project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ldbox.site.settings")

from django.core.wsgi import get_wsgi_application

path = '/usr/local/lib/python2/site-packages'
if path not in sys.path:
  sys.path.append(path)

application = get_wsgi_application()
