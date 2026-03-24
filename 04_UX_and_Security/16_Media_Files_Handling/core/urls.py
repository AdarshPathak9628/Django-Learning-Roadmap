from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from base_app import views

urlpatterns = [
    # Route for the Django Administration site
    path('admin/', admin.site.urls),
    # Root route to display the image gallery
    path('', views.gallery_view, name='gallery'),
]

# Serving media files during development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)