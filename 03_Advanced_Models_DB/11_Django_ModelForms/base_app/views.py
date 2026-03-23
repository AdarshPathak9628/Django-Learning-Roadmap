# base_app/views.py
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm # STEP 3: Import the form we just created

def home(request):
    # STEP 4: Check if user clicked the Submit button
    if request.method == "POST":
        form = StudentForm(request.POST) # Get the data from user
        if form.is_valid(): # Check if data is correct
            form.save() # Save data to Database
            return redirect('/') # Refresh the page
    
    # STEP 5: If it's a normal visit (GET), show blank form
    form = StudentForm()
    data = Student.objects.all() # Fetch all students to show in table
    
    return render(request, 'index.html', {'students': data, 'form': form})