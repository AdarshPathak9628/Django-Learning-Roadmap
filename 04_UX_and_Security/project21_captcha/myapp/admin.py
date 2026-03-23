from django.contrib import admin
from .models import student

# Register your models here.

class student_form(admin.ModelAdmin):

    list_display=('name','phone')

admin.site.register(student,student_form)