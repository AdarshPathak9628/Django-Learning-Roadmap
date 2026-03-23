from django.shortcuts import render

# Create your views here.

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('First_Number'))
            n2=eval(request.POST.get('Second_Number'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
            return render(request,'calculator.html',{'c':c,'n1':n1 ,'n2':n2})
    except:
        c="Invalid operation......"
    print(c)
    return render(request,'calculator.html',{'c':c})