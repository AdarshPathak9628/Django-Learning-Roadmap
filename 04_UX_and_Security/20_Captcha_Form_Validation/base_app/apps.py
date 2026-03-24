from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # This must match the real Django app folder name.
    name = 'base_app'
