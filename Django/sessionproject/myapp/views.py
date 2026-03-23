from django.shortcuts import render, redirect
from .models import session_model
from django.http import HttpResponseRedirect
import random

# Create your views here.

def login_view(request):
    u=request.session.get('username')
    p=request.session.get('password')
    if u and p:
        return HttpResponseRedirect('/dashboard/')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username and password match in your session_model
        try:
            user_data = session_model.objects.get(username=username, password=password)
            print(user_data)
            print("hello")
        except session_model.DoesNotExist:
            user_data = None
        
        if user_data is not None:
            # Set session data
            request.session['username'] = user_data.username
            request.session['email'] = user_data.email
            request.session['first_name'] = user_data.first_name
            request.session['last_name'] = user_data.last_name
            request.session.set_expiry(0)          
            return HttpResponseRedirect('/dashboard/') 
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        if password1 != password2:
            error_message = "Passwords do not match."
            return render(request, 'register.html', {'error_message': error_message})
        
        try:
            # Create the session_model instance
            new_session = session_model(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                address=address
            )
            # Save the instance to the database
            new_session.save()
            
            return HttpResponseRedirect('/login/')  # Redirect to the login page
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'register.html', {'error_message': error_message})
        
    return render(request, 'register.html')

def forget_view(request):
    return render(request,"forget.html")


# def forget_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
        
#         # Check if the email exists in the database
#         try:
#             user = User.objects.get(email=email)
#             # Generate and send OTP to the user's email
#             otp = generate_otp()  # Implement this function to generate OTP
#             send_otp_email(email, otp)  # Implement this function to send OTP via email
#             # Store OTP in session
#             request.session['otp'] = otp
#             return render(request, 'otp.html')
#         except User.DoesNotExist:
#             error_message = "Email not found in our records."
#             return render(request, 'forget.html', {'error_message': error_message})
#     else:
#         return render(request, 'forget.html')
    
# def otp_view(request):
#     return render(request,"otp.html")

def otp_view(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        
        # Check if OTP matches the one sent to the user
        if otp == request.session.get('otp'):
            # OTP matched, proceed with login
            del request.session['otp']  # Remove OTP from session after successful verification
            
            # Get user data from session_model based on OTP validation
            user_data = None  # Implement your logic to fetch user data
            
            if user_data is not None:
                # Set session data
                request.session['username'] = user_data.username
                request.session['email'] = user_data.email
                request.session['first_name'] = user_data.first_name
                request.session['last_name'] = user_data.last_name
                request.session.set_expiry(0)  # Optionally set session expiry time
                return HttpResponseRedirect('/dashboard/')
            else:
                error_message = "User data not found."
                return render(request, 'otp.html', {'error_message': error_message})
        else:
            error_message = "Invalid OTP."
            return render(request, 'otp.html', {'error_message': error_message})
    else:
        return render(request, 'otp.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')



def generate_otp():
    otp = ''.join(random.choices('0123456789', k=6))
    return otp
