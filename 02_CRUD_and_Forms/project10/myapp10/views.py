from django.shortcuts import render
from .models import student

# Create your views here.

# View to fetch all students from the database and display them
def show_students(request):
    # Fetching all records from the student table
    all_students = student.objects.all()
    
    # Passing the data to the template
    return render(request, 'students_list.html', {'students': all_students})