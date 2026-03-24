from django.db import models

# Professional Model to store User Information and Documents
class UserProfile(models.Model):
    # EmailField provides automatic email validation
    email = models.EmailField(max_length=100)
    # CharField for passwords (In real projects, use Django's built-in Auth)
    password = models.CharField(max_length=100)
    # FileField to store uploaded images in the 'images/' directory
    image = models.FileField(upload_to='images/')
    # Qualification details of the user
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.email