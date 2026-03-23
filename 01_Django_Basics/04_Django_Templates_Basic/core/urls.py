from django.contrib import admin
from django.urls import path, include # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # STEP: Change 'myapp4.urls' to 'base_app.urls'
    path('', include('base_app.urls')), 
]