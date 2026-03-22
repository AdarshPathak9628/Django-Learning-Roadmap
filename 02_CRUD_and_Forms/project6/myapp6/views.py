from django.shortcuts import render

# Create your views here.

# View to render the base layout (Master page)
def master(request):
    """Loads the main master layout"""
    return render(request, 'master.html')

# View to render the Home page content
def home(request):
    """Loads the home page template"""
    return render(request, 'home.html')

# View to render the About page content
def about(request):
    """Loads the about page template"""
    return render(request, 'about.html')

# View to render the Contact page content
def contact(request):
    """Loads the contact page template"""
    return render(request, 'contact.html')