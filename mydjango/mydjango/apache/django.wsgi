import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'mydjango.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/home/ss/mydjango/mydjango'
if path not in sys.path:
    sys.path.append(path)
