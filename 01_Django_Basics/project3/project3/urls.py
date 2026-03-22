from django.contrib import admin
from django.urls import path
from myapp3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test_views, name='test'),  # Corrected line
    path('test1/',views.test)
]

