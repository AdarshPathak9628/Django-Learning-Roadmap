from django.shortcuts import render

# Create your views here.

# Function to display the Home page
def home(request):
    """Returns the home.html template"""
    return render(request, 'home.html')

# Function to display the About page
def about(request):
    """Returns the about.html template"""
    return render(request, 'about.html')

# Function to display the Contact page
def contect(request):
    """Returns the contect.html template"""
    return render(request, 'contect.html')