from django.http import HttpResponse

# STEP 6: Simple Logic to show a message
def home_view(request):
    return HttpResponse("<h1 style='color: blue;'>Project 1: Professional Setup Success!</h1>")