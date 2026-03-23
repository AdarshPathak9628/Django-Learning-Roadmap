from django.apps import AppConfig

class BaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # STEP 1: Define the professional app name
    name = 'base_app'