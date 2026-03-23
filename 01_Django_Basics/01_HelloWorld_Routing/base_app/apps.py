from django.apps import AppConfig

class BaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # This name MUST match your folder name exactly
    name = 'base_app'