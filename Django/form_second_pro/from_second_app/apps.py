from django.apps import AppConfig


class FromSecondAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'from_second_app'
