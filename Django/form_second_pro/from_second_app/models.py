from django.db import models

# Create your models here.

class Student_Register(models.Model):
    first_name=models.CharField(max_length=100)
    second_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    


