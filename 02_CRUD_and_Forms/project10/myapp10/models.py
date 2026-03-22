from django.db import models

# Create your models here.

# Model to store Student information in the database
class student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=100)

    # This method displays the student's name in the Django Admin panel
    def __str__(self):
        return self.name