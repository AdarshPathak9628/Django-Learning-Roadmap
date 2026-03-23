# core/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# STEP 2: Update path to 'core.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()