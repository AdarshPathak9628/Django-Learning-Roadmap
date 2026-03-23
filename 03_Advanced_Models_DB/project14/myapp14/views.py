from django.shortcuts import render
from .forms import myform

# Create your views here.

def index_view(request):
    fm=myform()
    return render(request,'index.html',{'form':fm})