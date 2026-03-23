"""
URL Configuration for Project 5
This file maps the web browser addresses to specific view functions.
"""
from django.contrib import admin
from django.urls import include, path
from base_app import views

urlpatterns = [
    # Route for the Django admin panel
    path('admin/', admin.site.urls),
    path('', include('base_app.urls')), # Ensure this is base_app
    
    # Root URL: Loads the home page
    path('', views.home),
    
    # URL for the About page
    path('about/', views.about),
    
    # URL for the Contact page
    path('contect/', views.contect),
]