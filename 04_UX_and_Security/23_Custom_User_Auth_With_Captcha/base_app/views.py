from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        # SignupForm checks user data and captcha together.
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # LoginForm checks login fields and captcha.
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # get_user() returns the authenticated user from the form.
            user = form.get_user()
            # login() creates a session for the authenticated user.
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# login_required stops non-logged-in users from opening the home page.
@login_required(login_url='/')
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    # logout() removes the current user session.
    logout(request)
    return redirect('login')
