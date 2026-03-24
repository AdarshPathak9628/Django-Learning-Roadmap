from django.shortcuts import render

# Create your views here.

def set_cookie(request):
    response = render(request, "set.html")
    response.set_cookie('user', 'adarsh')
    return response

def get_cookie(request):
    cn = request.COOKIES.get('user', 'guest')
    return render(request, "get.html", {'cn': cn})

def set_operation(request):
    if request.method == "POST":
        title1 = request.POST.get('uname')
        color1 = request.POST.get('color')
        response = render(request, "set.html")
        response.set_cookie('title', title1)
        response.set_cookie('color', color1)
        return response
    return render(request, "set.html")

def get_operation(request):
    un = request.COOKIES.get('title', 'guest')
    col = request.COOKIES.get('color', 'white')
    return render(request, "get.html", {'un': un, 'col': col})
