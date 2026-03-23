from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        # Logic to handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        # Your authentication logic here
        if username == 'your_username' and password == 'your_password':
            # Login successful
            # Redirect to home page
            return redirect('home')
        else:
            # Login failed
            # Return to login page with an error message
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        # Render the login page
        return render(request, 'login.html')

def logout_view(request):
    # Your logout logic here
    # Redirect to login page after logout
    return redirect('login')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def store(request):
    return render(request, 'store.html')
