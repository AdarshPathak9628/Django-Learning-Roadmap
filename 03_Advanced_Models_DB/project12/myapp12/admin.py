from django.contrib import admin
from myapp12.models import student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','roll','name','course')
admin.site.register(student)