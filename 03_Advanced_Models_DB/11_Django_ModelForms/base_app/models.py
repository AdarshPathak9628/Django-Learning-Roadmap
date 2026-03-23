# base_app/models.py
from django.db import models

# ==========================================================
# STEP 7: DEFINE DATABASE TABLE
# ==========================================================
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_no = models.IntegerField()

    # STEP 8: Show the name in Admin panel instead of 'Object'
    def __str__(self):
        return self.name