from django.shortcuts import render, redirect
from .models import Student

def home(request):
    all_students = Student.objects.all()
    # Ensure 'home.html' name is spelled correctly here
    return render(request, 'home.html', {'students': all_students})

def update_student(request, id):
    # 1. Get the specific student from DB using ID
    student = Student.objects.get(id=id)

    if request.method == "POST":
        # 2. Get new data from the form
        student.name = request.POST.get('s_name')
        student.roll_no = request.POST.get('s_roll')
        student.email = request.POST.get('s_email')
        
        # 3. Save the changes
        student.save()
        return redirect('/')

    # 4. Pass the 'student' object to the form to show old data
    return render(request, 'update.html', {'student': student})