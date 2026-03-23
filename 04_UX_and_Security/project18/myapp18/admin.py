from django.contrib import admin
from .models import index_modal

# Register your models here.

class index_admin(admin.ModelAdmin):
    list_display=('id','email','password','image','qualification')

admin.site.register(index_modal,index_admin)