from django.db import models

# Create your models here.

class index_modal(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    image=models.FileField(upload_to='images/')
    qualification=models.CharField(max_length=100)