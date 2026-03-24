from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile

# View to Create new records and Display the list
def index_view(request):
    if request.method == 'POST':
        # Fetching data from POST request
        email_val = request.POST.get('email')
        pass_val = request.POST.get('password')
        qual_val = request.POST.get('res')
        img_val = request.FILES.get('image')
        
        # Saving the new instance to the database
        data = UserProfile(email=email_val, password=pass_val, qualification=qual_val, image=img_val)
        data.save()
        return redirect('index') # Refreshing the page after save

    # Fetching all records to display on the main page
    all_users = UserProfile.objects.all()
    
    # Process qualifications for each user
    for user in all_users:
        if user.qualification:
            user.qual_list = [q.strip() for q in user.qualification.split(',') if q.strip()]
        else:
            user.qual_list = []
    
    return render(request, 'index.html', {'users': all_users})

# View to Edit/Update an existing record
def edit_view(request, id):  
    # Using get_object_or_404 for better error handling
    obj = get_object_or_404(UserProfile, id=id)
    
    if request.method == "POST":
        # Updating the object fields
        obj.email = request.POST.get('email')
        obj.password = request.POST.get('password')
        
        # Checking if a new image was uploaded
        if 'image' in request.FILES:
            obj.image = request.FILES['image']
            
        obj.save()
        # Redirecting back to the home page after successful update
        return redirect('index')
    
    return render(request, 'edit.html', {'user': obj})