from django.shortcuts import render
from myapp13.models import Employee
# Create your views here.

def display_data(request):
    sts=Employee.objects.all()
    return render(request,"index.html",{'sts':sts})

