from django.shortcuts import render, redirect
from .models import Student

def home(request):
    # Check if the user clicked the 'Save' button
    if request.method == "POST":
        # Get data from HTML input names
        name_from_form = request.POST.get('s_name')
        roll_from_form = request.POST.get('s_roll')
        email_from_form = request.POST.get('s_email')

        # Save this data into the Database Model
        Student.objects.create(
            name = name_from_form,
            roll_no = roll_from_form,
            email = email_from_form
        )
        return redirect('/') # Refresh the page to show new data

    # Fetch all students to show them below the form
    all_students = Student.objects.all()
    return render(request, 'home.html', {'students': all_students})