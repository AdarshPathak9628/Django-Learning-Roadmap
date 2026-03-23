from django.shortcuts import render,redirect
from .models import index_modal
from django.http import HttpResponseRedirect

# Create your views here.

def index_view(request):
    if request.method=='POST':
        e=request.POST.get('email')
        p=request.POST.get('password')
        q=request.POST.get('res')
        i=request.FILES.get('image')
        data=index_modal(email=e,password=p,qualification=q,image=i)
        data.save()
    im=index_modal.objects.all()
    return render(request,'index.html',{'im':im})

def edit_view(request,id):  
    obj=index_modal.objects.get(id=id)
    if request.method=="POST":
        obj.email=request.POST.get('email')
        obj.password=request.POST.get('password')
        obj.image=request.FILES['image']
        print(obj.email,obj.password)
        # user=index_modal(id=id,email=e,password=p,image=i)
        obj.save()
        #return redirect('index')
        return HttpResponseRedirect('')
    
    return render(request,'edit.html',{'im':obj})
