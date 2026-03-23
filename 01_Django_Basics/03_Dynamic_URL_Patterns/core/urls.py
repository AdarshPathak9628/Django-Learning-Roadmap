from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # STEP 4: Directing traffic to base_app
    path('', include('base_app.urls')),
]