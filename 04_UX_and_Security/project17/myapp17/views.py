from django.shortcuts import render
from .models import img_modal
# Create your views here.

def Imageview(request):
    im=img_modal.objects.all()
    return render(request,'img.html',{'im':im})