from django.apps import AppConfig

class CbvAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cbv_app' # This should match the app name in INSTALLED_APPS in settings.py