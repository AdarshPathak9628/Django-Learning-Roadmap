from django.shortcuts import render, redirect
from .models import Student

def home(request):
    # Logic to Add Student
    if request.method == "POST":
        name = request.POST.get('s_name')
        roll = request.POST.get('s_roll')
        email = request.POST.get('s_email')
        Student.objects.create(name=name, roll_no=roll, email=email)
        return redirect('/')

    # Logic to Show Students
    all_students = Student.objects.all()
    return render(request, 'home.html', {'students': all_students})

def delete_student(request, id):
    student_to_delete = Student.objects.get(id=id)
    student_to_delete.delete()
    return redirect('/')