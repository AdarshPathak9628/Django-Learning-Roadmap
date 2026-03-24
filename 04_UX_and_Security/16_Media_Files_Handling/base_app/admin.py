from django.contrib import admin
from .models import ImageGallery  
# Professional Admin Class for better admin interface
class ImageAdmin(admin.ModelAdmin):
    # Displaying relevant fields in the admin interface
    list_display = ('id', 'title', 'image')
    # Optional: add search functionality
    search_fields = ('title',)

# Registering the new model name
admin.site.register(ImageGallery, ImageAdmin)