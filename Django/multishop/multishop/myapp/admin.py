from django.contrib import admin
from .models import vendor_images

# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'image')

# admin.site.register(Category, CategoryAdmin)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'price', 'stock', 'image')

# admin.site.register(Product, ProductAdmin)

class VendorAdmin(admin.ModelAdmin):
    list_display=('name','image')

admin.site.register(vendor_images,VendorAdmin)