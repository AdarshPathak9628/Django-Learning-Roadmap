from django.db import models

# Create your models here.

class student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=40)

    def __str__(self):
        return self.name
