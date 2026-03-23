from django.apps import AppConfig

class BaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # STEP 1: Change 'myapp4' to 'base_app'
    name = 'base_app'