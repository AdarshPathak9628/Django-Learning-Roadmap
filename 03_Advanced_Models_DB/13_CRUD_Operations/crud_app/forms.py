from django import forms
from .models import Student

# STEP 5: Create a form based on the Student model
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']