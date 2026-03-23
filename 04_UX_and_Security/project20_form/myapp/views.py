from django.shortcuts import render,redirect
from .forms import StudentForm

# Create your views here.

def index(request):
    if request.method=="POST":
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    fm=StudentForm()
    return render(request,'index.html',{'fm':fm})
    