from django.db import models

# Create your models here.

class Emp_login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class Emp_signup(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    dob=models.DateField()
    occupation=models.CharField(max_length=100)
    country=models.CharField(max_length=100)