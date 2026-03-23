from django.contrib import admin
from .models import Student  # Import the Student model from models.py

# Register the Student model to make it visible in the Django Admin Panel
admin.site.register(Student)