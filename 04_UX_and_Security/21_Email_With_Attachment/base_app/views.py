from django.shortcuts import render, redirect
from django.core.mail import send_mail , EmailMessage
from django.conf import settings
from django.contrib import messages
#import random

def send_email(request):
    subject='account update'
    message=f"your otp is ....and dont share this otp "
    # We use this setting so the sender email comes from one central place.
    from_email=settings.EMAIL_HOST_USER
    # recipient_list=['adarshpathak9628@gmail.com']
    recipient_list=['abhitiwa1975@gmail.com']
    # BASE_DIR gives the main project folder path.
    file_path=f"{settings.BASE_DIR}/userr.txt"
    # send_mail() is a simple Django function for basic emails.
    #send_mail(subject,message,from_email,recipient_list)
    # EmailMessage is used when we need more control like file attachment.
    mail=EmailMessage(subject=subject,body=message, from_email=from_email, to=recipient_list)
    # attach_file() adds the selected file to the email.
    mail.attach_file(file_path)
    # send() sends the email to the receiver list.
    mail.send()
    # This print helps us see in terminal where the email was sent.
    print(f"Email sent to: {recipient_list[0]}")
    print(f"Message body: {message}")
    # messages.success() shows a success message on the next page load.
    messages.success(request, f"Email sent to {recipient_list[0]}")
    return redirect('/')   

def index(request):
    return render(request,"index.html")

