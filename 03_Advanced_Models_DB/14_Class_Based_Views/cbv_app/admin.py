from django.contrib import admin

# STEP 1: Change 'myapp15' to 'cbv_app'
from cbv_app.models import Emp_signup, Emp_login 

# STEP 2: Your existing admin logic (No change needed here)
class Emp_login_admin(admin.ModelAdmin):
   list_display = ('username', 'password')

class Emp_signup_admin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'phone', 'address', 'dob', 'occupation', 'country')

admin.site.register(Emp_login, Emp_login_admin)
admin.site.register(Emp_signup, Emp_signup_admin)