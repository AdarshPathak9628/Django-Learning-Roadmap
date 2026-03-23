from django.db import models

# Create your models here.

class Emp_login(models.Model):
    username=models.CharField(max_length=100,null=True)
    password=models.IntegerField(max_length=100,null=True)

class Emp_signup(models.Model):
    eid=models.IntegerField(null=True)
    name=models.CharField(max_length=100,null=True)
    password=models.IntegerField(max_length=100,null=True)
    email=models.EmailField(null=True)
    