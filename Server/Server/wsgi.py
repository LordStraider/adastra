import sys, os
print  >>sys.stderr, "hej from wsgi.py"
sys.path.append('/home/Wedmod/www/djangojquerycontroller/Server')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Server.settings")
print >>sys.stderr, 'path: '
print >>sys.stderr, sys.path
print >>sys.stderr, '   end of path!   '
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler( )

