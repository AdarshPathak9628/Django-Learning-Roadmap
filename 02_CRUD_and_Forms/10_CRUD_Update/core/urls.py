from django.contrib import admin
from django.urls import path, include # Import include to connect the app

urlpatterns = [
    # 1. Standard Django Admin URL
    path('admin/', admin.site.urls),
    
    # 2. Connect all URLs from our 'base_app'
    path('', include('base_app.urls')),
]