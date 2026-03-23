from django.contrib import admin
from myapp15.models import Emp_signup,Emp_login

# Register your models here.

class Emp_login_admin(admin.ModelAdmin):
   list_display=('username','password')

class Emp_signup_admin(admin.ModelAdmin):
    list_display=('username','email','password','phone','address','dob','occupation','country')

admin.site.register(Emp_login,Emp_login_admin)
admin.site.register(Emp_signup,Emp_signup_admin)