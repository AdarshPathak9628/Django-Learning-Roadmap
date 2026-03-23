from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Category,Product,Customer
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
# Create your views here.
class Index(View):
    def post(self,request):
        pcart=request.session.get('cart',{})
        pid=request.POST.get('addproduct')
        rm=request.POST.get('remove')
        if pcart:
            qty=pcart.get(pid)
            if qty:
                    if rm:
                        if qty<=1:
                            pcart.pop(pid)
                        else:
                            qty=qty-1
                            pcart[pid]=qty    
                    else:
                        qty=qty+1
                        pcart[pid]=qty
            else:
                pcart[pid]=1    
        else:
            pcart[pid]=1
        request.session['cart']=pcart
        print(request.session.get('cart'))
        return redirect('/')
    def get(self,request):
        cid=request.GET.get('category')
        if cid:
           prods=Product.objects.filter(category=cid)
        else:
           prods=Product.objects.all()   
        cats=Category.objects.all()
        data={'prods':prods,'cats':cats}
        return render(request,"index.html",data)

def admin_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        upass=request.POST.get('password')
        if uname=='admin' and upass=='12345':
            return redirect('/dashboard/')
        else:
            return HttpResponse("Invalid username or Password!!!")
    return render(request,"admin_login.html")


def dashboard_view(request):
    return render(request,"dashboard.html")

def addproduct_view(request):
    if request.method=="POST":
        pname=request.POST.get('name')
        price=request.POST.get('price')
        cat=request.POST.get('category')
        des=request.POST.get('des')
        img=request.FILES['imag']
        cobj=Category.objects.get(id=cat)
        pobj=Product(name=pname,price=price,category=cobj,des=des,image=img)
        pobj.save()
        return redirect('/viewproduct/')
    cats=Category.objects.all()
    return render(request,"addproduct.html",{'cats':cats})

def viewproduct_view(request):
    prods=Product.objects.all()
    return render(request,'viewproduct.html',{'prods':prods})


def deleteproduct_view(request,id):
    rec=Product.objects.get(id=id)
    rec.delete()
    os.remove(rec.image.path)
    return redirect('/viewproduct/')

def addcategory_view(request):
    if request.method=="POST":
        cname=request.POST.get('name')
        des=request.POST.get('des')
        cobj=Category(name=cname,des=des)
        cobj.save()
    return render(request,"addcategory.html")

def signup_view(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        father=request.POST.get('father')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        phone=request.POST.get('phone')
        img=request.FILES['imag']
        if pass1==pass2:
            cobj=Customer(fname=fname,lname=lname,father=father,email=email,pass1=pass1,Phone=phone,image=img)
            cobj.pass1=make_password(cobj.pass1)
            cobj.save()
            return redirect('/')
        else:
            return HttpResponse("Password did not match")   
    return render(request,"signup.html")

def userlogin_view(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        upass=request.POST.get('password')
        cust=Customer.objects.get(email=uname)   
        if cust:
            if uname==cust.email and check_password(upass,cust.pass1):
                request.session['cust_id']=cust.id
                request.session['cust_name']=cust.fname
                request.session['cust_email']=cust.email
                return redirect('index')
        else:
            pass
    return render(request,"userlogin.html")


def logout_view(request):
    request.session.clear()
    return redirect('/')

@login_required(login_url='/userlogin/')
def cart_view(request):
    ids=[]
    try:
        ids=list(request.session.get('cart').keys())
    except:
        pass    
    prods=Product.objects.filter(id__in=ids)
    return render(request,"cart.html",{'prods':prods})