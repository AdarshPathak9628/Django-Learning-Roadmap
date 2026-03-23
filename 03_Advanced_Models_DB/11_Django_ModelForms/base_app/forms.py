# base_app/forms.py
from django import forms
from .models import Student # STEP 1: Import your Model

# ==========================================================
# STEP 2: CREATE MODEL FORM
# This class tells Django to create a form based on Student table.
# ==========================================================
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student # Use the Student table
        fields = ['name', 'email', 'roll_no'] # Fields you want in the form