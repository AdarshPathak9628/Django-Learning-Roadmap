from django.contrib import admin
from .models import Customer,Category,Product
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=('fname','lname','father','email','pass1','Phone','image')

admin.site.register(Customer,CustomerAdmin)  

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','des')

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','price','category','des','image')

admin.site.register(Product,ProductAdmin)