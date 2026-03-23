from django.shortcuts import render
from .models import Student_Register

# Create your views here.

def login_view(request):
    return render(request,'login.html')

def register_view(request):
    if(request.method=='post'):
        fn=request.POST.get('first_name')
        sn=request.POST.get('second_name')
        e=request.POST.get('email')
        p=request.POST.get('password')
        cp=request.POST.get('confirm_password')
       # obj=Student_Register(fn=first_name,sn=second_name,e=email,p=password,cp=confirm_password)
        #obj.save()
    return render(request,'register.html')

def index_view(request):
    return render(request,'index.html')

def home_view(request):
    return render(request,'home.html')