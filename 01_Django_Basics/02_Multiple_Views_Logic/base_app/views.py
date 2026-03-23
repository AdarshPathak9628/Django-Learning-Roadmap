from django.http import HttpResponse

# STEP 3: Create functions for different pages
def home(request):
    return HttpResponse("<h1>Home Page</h1><p>Welcome to Project 2</p>")

def about(request):
    return HttpResponse("<h1>About Page</h1><p>This project has multiple views.</p>")

def contact(request):
    return HttpResponse("<h1>Contact Page</h1><p>Email: adarsh@lpu.in</p>")