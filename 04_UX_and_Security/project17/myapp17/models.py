from django.db import models

# Create your models here.

class img_modal(models.Model):
    title=models.CharField(max_length=100)
    image=models.FileField(upload_to='images/')