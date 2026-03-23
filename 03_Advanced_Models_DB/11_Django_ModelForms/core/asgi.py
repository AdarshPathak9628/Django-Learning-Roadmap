# core/asgi.py
import os
from django.core.asgi import get_asgi_application

# STEP 3: Update path to 'core.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()