"""
URL Configuration for Project 6
Maps web addresses to the views in myapp6.
"""
from django.contrib import admin
from django.urls import path
from myapp6 import views

urlpatterns = [
    # Admin dashboard route
    path('admin/', admin.site.urls),
    
    # Root URL: Default master page
    path('', views.master),
    
    # Named routes for easy linking in templates
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]