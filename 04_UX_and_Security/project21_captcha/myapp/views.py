from django.shortcuts import render, redirect
from .forms import StudentForm

def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = StudentForm()

    return render(request, 'index.html', {'form': form})
