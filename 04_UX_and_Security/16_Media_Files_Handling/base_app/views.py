from django.shortcuts import render
from .models import ImageGallery

# View to retrieve and display all images in the gallery
def gallery_view(request):
    # Querying all records from the ImageGallery database table
    images = ImageGallery.objects.all()
    # Passing the queryset to the template context
    context = {'images': images}
    return render(request, 'img.html', context)