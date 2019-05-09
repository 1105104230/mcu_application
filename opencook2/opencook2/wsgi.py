"""
WSGI config for opencook2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opencook2.settings")

# application = get_wsgi_application()

import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opencook2.settings")　#host的靜態檔案 不使用runserver
application = Cling(get_wsgi_application())

