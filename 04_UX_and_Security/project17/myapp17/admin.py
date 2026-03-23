from django.contrib import admin
from .models import img_modal

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display=('id','title','image')
admin.site.register(img_modal,ImageAdmin)