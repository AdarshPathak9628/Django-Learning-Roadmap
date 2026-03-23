from django.contrib import admin
from .models import Student

# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display=('name','phone')

admin.site.register(Student,studentadmin)