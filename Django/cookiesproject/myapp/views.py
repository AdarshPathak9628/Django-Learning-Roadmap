from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import sign_model 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        response=render(request,"login.html")
        obj=sign_model.objects.all()
        for i in obj:
            if username == i.user_name and password == i.password:
                response.set_cookie('user',username)
                response.set_cookie('paas',password)
                return response
            #return redirect('welcome')    
        else:
            return HttpResponse("Invalid Credentials")     
    return render(request, 'login.html')


def sign_view(request):
    if(request.method=="POST"):
        fn=request.POST.get('first_name')
        ln=request.POST.get('last_name')
        un=request.POST.get('username')
        e=request.POST.get('email')
        p=request.POST.get('password')
        c=request.POST.get('confirm_password')
        d=request.POST.get('dob')
        if(p==c):
            obj=sign_model(first_name=fn,last_name=ln,user_name=un,email=e,password=p,dob=d)
            obj.save()  
            return render(request,"login.html")    
    return render(request,"sign.html")

def forget_view(request):
    return render(request,"forget.html")

def otp_view(request):
    return render(request,"otp.html")

def welcome_view(request):
    user1 = request.COOKIES.get('user')
    paas = request.COOKIES.get('paas')
    print(user1)
    if user1 and paas:
        return render(request, "welcome.html", {'un': user1})
    else:
        return render(request, "login.html")


def logout_view(request):
    response = render(request, 'logout.html')
    user = request.COOKIES.get('user')
    paas = request.COOKIES.get('paas')
    if user and paas:
        response.delete_cookie('user')
        response.delete_cookie('paas')
        return response
    return render(request,"logout.html")
    
def profile_view(request):
    user1 = request.COOKIES.get('user')
    return render(request,'profile.html',{'un':user1})