from django.shortcuts import render
from myapp15.models import Emp_signup

# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        try:
            user = list(Emp_signup.objects.all())
        except Emp_signup.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username or password111'})
        for i in user:
            print(i.username,i.password)
            print(u,p)
            print('i am not working')
            if(str(i.username)==str(u) and str(i.password)==str(p)):
                print("password matched")
                return render(request,'profile.html')
            else:
               return render(request, 'login.html', {'error': 'Invalid username or password'})        
    return render(request, 'login.html')

def signup(request):
    if(request.method=='POST'):
        un=request.POST.get('username')
        e=request.POST.get('email')
        p=request.POST.get('password')
        ph=request.POST.get('phone')
        a=request.POST.get('address')
        d=request.POST.get('dob')
        o=request.POST.get('occupation')
        c=request.POST.get('country')
        print(un,e)
        obj=Emp_signup(username=un,email=e,password=p,phone=ph,address=a,dob=d,occupation=o,country=c)
        obj.save()
    return render(request,'signup.html')

def profile(request):
    return render(request,'profile.html')