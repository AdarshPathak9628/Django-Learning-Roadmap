from django.contrib import admin
from .models import student

# Register your models here.

# Customizing how the student model appears in the Admin area
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll', 'name') # Shows both columns in the admin list

admin.site.register(student, StudentAdmin)