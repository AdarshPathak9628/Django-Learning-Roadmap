from django.contrib import admin
# STEP 1: Update the app name from 'myapp13' to 'pages_app'
from pages_app.models import Employee 

# STEP 2: Professional Admin configuration
class EmployeeAdmin(admin.ModelAdmin):
    # This shows these columns in the Django Admin list
    list_display = ('id', 'eid', 'name', 'company') 

# STEP 3: Register the model
admin.site.register(Employee, EmployeeAdmin)