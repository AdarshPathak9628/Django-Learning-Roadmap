from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.

def index(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = StudentForm()

    students = Student.objects.all()
    return render(request, 'index.html', {'fm': fm, 'students': students})
    