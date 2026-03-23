from django.shortcuts import render

from .forms import Mysignup,Mylogin
from .models import Emp_login,Emp_signup

# Create your views here.

def login(request):
    fm=Mylogin()
    u=request.GET.get('username')
    p=request.GET.get('password')
    print(u,p)
    obj=Emp_login(username=u,password=p)
    obj.save()
    return render(request,'login.html',{'form':fm})

def signup(request):
    sfm=Mysignup()
    i=request.GET.get('eid')
    n=request.GET.get('name')
    p=request.GET.get('password')
    e=request.GET.get('email')
    print(i,n,p,e)
    obj=Emp_signup(eid=i,name=n,password=p,email=e)
    obj.save()
    return render(request,'singup.html',{'sform':sfm})