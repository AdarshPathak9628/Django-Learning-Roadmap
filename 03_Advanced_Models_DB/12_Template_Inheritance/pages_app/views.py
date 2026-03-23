# pages_app/views.py
from django.shortcuts import render
from .models import Employee # STEP 1: Import your Model

# ==========================================================
# STEP 2: DEFINE THE VIEW FUNCTION
# Make sure the name is 'display_data' to match your urls.py
# ==========================================================
def display_data(request):
    # Fetching all employee records
    sts = Employee.objects.all() 
    
    # STEP 3: Render the index.html template
    return render(request, 'index.html', {'sts': sts})