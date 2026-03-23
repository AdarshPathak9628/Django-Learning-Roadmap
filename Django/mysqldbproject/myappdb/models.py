from django.db import models

# Create your models here.

class Student(models.Model):
    roll=models.IntegerField(max_length=100)
    sname=models.CharField(max_length=100)