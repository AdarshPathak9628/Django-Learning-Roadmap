from django.contrib import admin
from .models import Student  # Import your Student model

# Register the Student model to make it visible in the Admin Panel
admin.site.register(Student)