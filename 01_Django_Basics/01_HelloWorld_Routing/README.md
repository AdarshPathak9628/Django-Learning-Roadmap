Project 01: Professional Django Setup Guide
This project is the foundation of Django. We have used a professional "Core-App" structure. Follow these simple steps to understand how this project works.

Step 1: Internal App Identity
File: base_app/apps.py
This file tells Django the official name of your app. The name here must match your folder name.

Python
from django.apps import AppConfig

class BaseAppConfig(AppConfig):
default_auto_field = 'django.db.models.BigAutoField'
name = 'base_app' # Internal identity of the app
Step 2: Registering the App
File: core/settings.py
In this file, we add our app name to the INSTALLED_APPS list. If you don't do this, Django will not recognize your app.

Python
INSTALLED_APPS = [
...
'base_app', # Connecting our app to the main project
]
Step 3: Main URL Controller (Main Gate)
File: core/urls.py
This is the first place the browser visits. We tell this file to send all requests to our base_app.

Python
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('base_app.urls')), # Forwarding request to base_app
]
Step 4: App URL Map (Local Gate)
File: base_app/urls.py
This file is inside your app. It maps the empty path to a specific logic (View).

Python
from django.urls import path
from . import views

urlpatterns = [
path('', views.home_view, name='home'), # Linking path to home_view function
]
Step 5: The Brain (Logic Layer)
File: base_app/views.py
This is where the actual logic happens. It takes the request and sends back a response.

Python
from django.http import HttpResponse

def home_view(request): # This message is displayed on the browser screen
return HttpResponse("<h1>Success: Professional Routing Setup!</h1>")
Step 6: How to Run the Project
Open Terminal in the folder: 01_Django_Basics/01_HelloWorld_Routing

Activate your Environment: .\venv\Scripts\activate

Install Django (if not already): pip install django

Start the Server: python manage.py runserver

Open Link: http://127.0.0.1:8000/
