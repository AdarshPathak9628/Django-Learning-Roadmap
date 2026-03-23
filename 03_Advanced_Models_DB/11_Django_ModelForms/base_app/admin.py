from django.contrib import admin
# STEP 3: Import your model using the new app path
from base_app.models import Student 

# STEP 4: Register model to see it in Admin Panel
admin.site.register(Student)