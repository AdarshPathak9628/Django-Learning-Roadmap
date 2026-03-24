"""
URL configuration for 22_Django_User_Authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base_app import views

urlpatterns = [
    # Home page is protected and opens only after login.
    path('', views.home, name='home'),
    # Login page for existing users.
    path('login/', views.login_view, name='login'),
    # Signup page for new users.
    path('signup/', views.signup, name='signup'),
    # Logout clears the current user session.
    path('logout/', views.logout_view, name='logout'),
]
