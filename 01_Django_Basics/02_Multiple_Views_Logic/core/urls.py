from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # STEP 5: Connect base_app urls
    path('', include('base_app.urls')),
]