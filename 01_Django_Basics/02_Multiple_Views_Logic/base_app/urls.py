from django.urls import path
from . import views

urlpatterns = [
    # STEP 4: Mapping URLs to views
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]