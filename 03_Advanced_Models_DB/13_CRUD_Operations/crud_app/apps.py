# STEP 1: Add this import line!
from django.apps import AppConfig

# STEP 2: Make sure the name matches 'crud_app'
class CrudAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crud_app'