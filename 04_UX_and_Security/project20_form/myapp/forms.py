from django import forms
from .models import Student  # Ensure your import matches the model name

class StudentForm(forms.ModelForm):  # Class name in CamelCase

    class Meta:
        model = Student  # Model name capitalized
        fields = ['name', 'phone']  # Corrected 'field' to 'fields'

