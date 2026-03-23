from django.http import HttpResponse

# STEP 2: Logic to capture data from URL
def home(request):
    return HttpResponse("<h1>Project 3: Dynamic URLs</h1><p>Try /user/Adarsh/ or /roll/22/</p>")

def user_view(request, username):
    # 'username' is dynamic text from URL
    return HttpResponse(f"<h1>Profile Page</h1><p>Welcome, <b>{username}</b>! Your name is fetched from the URL.</p>")

def roll_view(request, roll_no):
    # 'roll_no' is a dynamic number from URL
    return HttpResponse(f"<h1>Student Portal</h1><p>Data for Roll Number: <b>{roll_no}</b></p>")