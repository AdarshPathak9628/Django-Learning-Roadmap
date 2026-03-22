from django.contrib import admin
from django.urls import path
from myapp10 import views # Import views from myapp10

urlpatterns = [
    path('admin/', admin.site.urls),
]