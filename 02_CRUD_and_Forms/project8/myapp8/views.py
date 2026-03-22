from django.shortcuts import render

# Create your views here.

# Main landing page view
def index(request):
    """Renders the main structure of the site"""
    return render(request, 'index.html')

# Home page view with Carousel
def home(request):
    """Loads the home page content"""
    return render(request, 'home.html')

# About page view
def about(request):
    """Loads information about the project"""
    return render(request, 'about.html')

# Services page view
def services(request):
    """Lists all available services"""
    return render(request, 'services.html')

# Team page view
def team(request):
    """Displays team member profiles"""
    return render(request, 'team.html')

# Contact page view
def contact(request):
    """Loads the contact information page"""
    return render(request, 'contact.html')