from django.shortcuts import render
from .models import Student # Import your Model

def home(request):
    # Fetch all student records from the database
    all_students = Student.objects.all()
    
    # Send the data to the template using a dictionary
    return render(request, 'home.html', {'students': all_students})