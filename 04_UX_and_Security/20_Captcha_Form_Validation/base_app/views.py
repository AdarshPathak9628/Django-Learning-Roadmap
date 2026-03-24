from django.shortcuts import render, redirect
from .forms import StudentForm

def index(request):
    # If the user submits the form, validate and save the data.
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        # Show an empty form when the page opens for the first time.
        form = StudentForm()

    return render(request, 'index.html', {'form': form})
