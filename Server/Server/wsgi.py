import sys, os

sys.path.append('/home/Webmod/www/djangojquerycontroller/Server')

os.environ["DJANGO_SETTINGS_MODULE"]="Server.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Server.settings")

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler( )

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
