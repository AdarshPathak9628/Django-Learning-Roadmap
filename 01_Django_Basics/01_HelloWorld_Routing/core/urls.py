from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # STEP 4: Forwarding all home requests to base_app
    path('', include('base_app.urls')), 
]