import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Server.settings")
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
