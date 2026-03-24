from django.contrib.auth.models import AbstractUser
from django.db import models

# AbstractUser gives us Django's default user fields and lets us customize them.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    
    # Add any additional fields here if necessary
    # Example: phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username
