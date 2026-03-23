from django.shortcuts import render

# Create your views here.

def SetCookie(request):
    response=render(request,"set.html")
    response.set_cookie('user','adarsh')
    return response

def GetCookie(request):
    cn=request.COOKIES.get('user','guest')
    return render(request,"get.html",{'cn':cn})

def setOPRATION(request):
    if request.method=="POST":
        title1=request.POST.get('name')
        color1=request.POST.get('color')
        response=render(request,"set.html")
        response.set_cookie('title',title1)
        response.set_cookie('color',color1)
        return response
    return render(request,"set.html")
def getOPRATION(request):
    un=request.COOKIES.get('title','guest')
    col=request.COOKIES.get('color')
    return render(request,"get.html",{'un':un,'title':t,'col':col})
