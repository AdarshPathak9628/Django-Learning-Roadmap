from django.urls import path
from . import views # '.' means current folder (base_app)

urlpatterns = [
    # Mapping the view to 'info/'
    path('info/', views.info_view, name='employee_info'),
]