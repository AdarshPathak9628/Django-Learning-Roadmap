from django.contrib import admin
from .models import Student  # Import your Student table from models.py

# This registers the Student model so it shows up in the Admin Panel
admin.site.register(Student)