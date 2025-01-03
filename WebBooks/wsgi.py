"""
WSGI config for WebBooks project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
# это настройки для timeweb хостинга
# import sys

# activate_this = os.path.expanduser("~/new-site/venv/bin/activate_this.py")
# exec(open(activate_this).read(), {"__file__": activate_this})

# sys.path.insert(1, os.path.expanduser("~/new-site/public_html/"))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebBooks.settings")

application = get_wsgi_application()
