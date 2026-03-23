from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# --- EXISTING INDEX VIEW ---
def index_view(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = StudentForm()
    students = Student.objects.all()
    return render(request, 'index.html', {'form': fm, 'students': students})

# --- STEP 1: DELETE LOGIC ---
def delete_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id) # Get the specific student by ID
        pi.delete() # Delete from database
        return redirect('/')

# --- STEP 2: EDIT LOGIC ---
def update_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        # Fill the form with existing data (instance=pi) + new data (request.POST)
        fm = StudentForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentForm(instance=pi) # Show form with old data filled in
    return render(request, 'update.html', {'form': fm})