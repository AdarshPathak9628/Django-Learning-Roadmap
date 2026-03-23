from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request,'login.html')

def signup_view(request):
    return render(request,'signup.html')

def forget_view(request):
    return render(request,'forget.html')

def otp_view(request):
    return render(request,'otp.html')