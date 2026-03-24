from django.db import models

# Model to handle image uploads and gallery metadata
class ImageGallery(models.Model):
    # Field to store the title of the image
    title = models.CharField(max_length=100)
    # Field to store the image file, uploaded to 'media/images/' directory
    image = models.FileField(upload_to='images/')

    def __str__(self):
        # Return the title as the object representation in Admin
        return self.title