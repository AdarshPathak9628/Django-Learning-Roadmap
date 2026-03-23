from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request,'index.html')

def login_view(request):
    email="adarsh@gmail.com"
    password=12345
    if request.method=="POST":
        email=request.POST.get('email_input')
        password=request.POST.get('password_input')
        return render(request,'login.html')
    
    return render(request,'login.html')

def signup_view(request):
    return render(request,'signup.html')

def forget_view(request):
    return render(request,'forget.html')

def otp_view(request):
    return render(request,'otp.html')
