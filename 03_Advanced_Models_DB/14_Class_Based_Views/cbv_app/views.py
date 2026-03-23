from django.shortcuts import render, redirect
from .models import Emp_signup

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from .models import Emp_signup

def signup(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        e = request.POST.get('email')
        p = request.POST.get('password')
        ph = request.POST.get('phone')
        a = request.POST.get('address')
        d = request.POST.get('dob')
        occ = request.POST.get('occupation')
        c = request.POST.get('country')

        # Step 2: Save to Database
        obj = Emp_signup(
            username=un, 
            email=e, 
            password=p, 
            phone=ph, 
            address=a, 
            dob=d, 
            occupation=occ, 
            country=c
        )
        obj.save()
        return redirect('login')
        
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        # EASY ENGLISH: Find the user
        user = Emp_signup.objects.filter(username=u, password=p).first()
        
        if user:
            return render(request, 'profile.html', {'user': user})
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
            
    return render(request, 'login.html')



def profile(request):
    return render(request, 'profile.html')