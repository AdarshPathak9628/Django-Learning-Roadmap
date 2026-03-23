from django.shortcuts import render

# Function to display the Home page
def home(request):
    return render(request, 'home.html')

# Function to display the About page
def about(request):
    return render(request, 'about.html')

# Function to display the Contact page
def contect(request):
    return render(request, 'contect.html')