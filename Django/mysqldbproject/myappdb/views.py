from django.shortcuts import render
from .models import Student

# Create your views here.
def save_data(request):
    if request.method=="POST":
        r=request.POST.get('roll')
        n=request.POST.get('sname')
        obj=Student(roll=r,name=n)
        obj.save()
    return render(request,'set.html')