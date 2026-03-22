from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    return HttpResponse("<h1> This is test program aur sabse phle views.py bana fir project ke urls me gye fir ye set karenge [  path('  yha pe ham name sakte hai jo 127.0.0.1/ yha lekhna hoga name ex = http://127.0.0.1:8000/test/       '    ,views.test)  ]  </h1>")
    
