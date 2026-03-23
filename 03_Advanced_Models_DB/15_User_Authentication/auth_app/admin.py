from django.contrib import admin
from .models import Emp_login,Emp_signup

# Register your models here.

class Emp_login_model(admin.ModelAdmin):
    list_display=('username','password')



class Emp_signup_model(admin.ModelAdmin):
    list_display=('eid','name','password','email')

admin.site.register(Emp_login,Emp_login_model)
admin.site.register(Emp_signup,Emp_signup_model)
