# core/urls.py
from django.contrib import admin
from django.urls import path
from pages_app import views # STEP 4: Import views from the new app name

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # STEP 5: Link the URL to the display_data function
    path('', views.display_data), 
]