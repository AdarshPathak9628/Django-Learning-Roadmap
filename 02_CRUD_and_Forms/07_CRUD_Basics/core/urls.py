from django.urls import path, include
from django.contrib import admin  # <--- ADD THIS LINE!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_app.urls')),
]