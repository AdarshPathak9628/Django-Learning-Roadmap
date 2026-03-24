Project 16: Professional Media Files Handling
This project demonstrates how to manage user-uploaded files (Images) in a Django application. It covers the configuration of MEDIA_URL, MEDIA_ROOT, and displaying database-stored images on a web page.

Project Structure
We follow a professional naming convention for better organization:

core/: Contains the main project settings (settings.py, urls.py, wsgi.py).

base_app/: Contains the application logic (models, views, admin).

media/images/: The directory where all uploaded images are stored.

Key Features
Dynamic Image Upload: Upload images via the Django Admin Panel.

Media Configuration: Professional setup for handling file paths in development.

Database Integration: Storing image metadata using Django Models.

Clean UI: Displaying a gallery of images with a fallback message if the database is empty.

Technical Implementation

1. Media Settings (core/settings.py)
   We define where the files should be stored on the computer and how they should be accessed via a URL.

Python

# The URL path to access media files in the browser

MEDIA_URL = '/media/'

# The actual folder path on the system to store uploaded files

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 2. Image Model (base_app/models.py)
Using FileField or ImageField to create a table for storing images.

Python
class ImageGallery(models.Model):
title = models.CharField(max_length=100) # Images will be saved inside 'media/images/'
image = models.FileField(upload_to='images/') 3. URL Routing (core/urls.py)
Connecting the media folder to the project's URL patterns.

Python

# Serving media files during development

if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
How to Run This Project
Activate Virtual Environment:
.\.venv\Scripts\Activate.ps1

Apply Migrations:
python manage.py makemigrations
python manage.py migrate

Create Superuser:
python manage.py createsuperuser

Run Server:
python manage.py runserver

Upload Data: Go to /admin, add images to the ImageGallery, and view them on the home page.
