"""
URL Configuration for Project 8
Maps all website pages to myapp8 views.
"""
from django.contrib import admin
from django.urls import path
from myapp8 import views

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),
    
    # Page Routes
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
]