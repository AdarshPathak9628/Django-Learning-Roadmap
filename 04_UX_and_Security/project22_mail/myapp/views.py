from django.shortcuts import render, redirect
from django.core.mail import send_mail , EmailMessage
from django.conf import settings
#import random

# Create your views here.
def send_email(request):
    subject='account update'
    message=f"your otp is ....and dont share this otp "
    from_email=settings.EMAIL_HOST_USER
    recipient_list=['myriadcodex@gmail.com']
    file_path=f"{settings.BASE_DIR}/userr.txt"
    #send_mail(subject,message,from_email,recipient_list)
    mail=EmailMessage(subject=subject,body=message, from_email=from_email, to=recipient_list)
    mail.attach_file(file_path)
    mail.send()
    return redirect('/')   

def index(request):
    return render(request,"index.html")


