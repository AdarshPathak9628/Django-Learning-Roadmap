# base_app/urls.py
from django.urls import path
from . import views # STEP 1: Import views from the same folder

urlpatterns = [
    # STEP 2: Link your home view
    path('', views.home, name='home'), 
]