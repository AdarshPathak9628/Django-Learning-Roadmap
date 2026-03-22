"""
URL Configuration for Project 5
This file maps the web browser addresses to specific view functions.
"""
from django.contrib import admin
from django.urls import path
from myapp5 import views

urlpatterns = [
    # Route for the Django admin panel
    path('admin/', admin.site.urls),
    
    # Root URL: Loads the home page
    path('', views.home),
    
    # URL for the About page
    path('about/', views.about),
    
    # URL for the Contact page
    path('contect/', views.contect),
]