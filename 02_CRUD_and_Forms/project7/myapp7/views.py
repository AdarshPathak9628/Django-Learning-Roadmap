from django.shortcuts import render

# Create your views here.

# Main landing page view
def index(request):
    """Renders the base index template"""
    return render(request, 'index.html')

# View to display the image page
def img(request):
    """Renders the template containing static images"""
    return render(request, 'img.html')