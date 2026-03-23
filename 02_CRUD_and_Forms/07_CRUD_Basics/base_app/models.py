from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    email = models.EmailField()

    # This MUST be inside the class (4 spaces from the left)
    # Use double underscore __ before and after str
    def __str__(self):
        return self.name