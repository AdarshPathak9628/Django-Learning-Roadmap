from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# 1. SIGNUP: Naya user banane ke liye
def signup_view(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST) 
        if fm.is_valid():
            fm.save() # Yeh sidha Admin Panel ke 'Users' mein save hoga
            return redirect('login')
    else:
        fm = UserCreationForm()
    return render(request, 'signup.html', {'sform': fm})

# 2. LOGIN: User check karne ke liye
def login_view(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})

# 3. PROFILE: Login ke baad dikhane ke liye
def profile_view(request):
    return render(request, 'profile.html')


def logout_view(request):
    logout(request) #  This destroys the session
    return redirect('login') # After logout, go back to login page

def profile_view(request):
    return render(request, 'profile.html')