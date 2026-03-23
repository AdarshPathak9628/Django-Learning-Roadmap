# core/urls.py
from django.contrib import admin
from django.urls import path, include # STEP 3: Must include 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # STEP 4: This looks for urls.py inside base_app
    path('', include('base_app.urls')), 
]