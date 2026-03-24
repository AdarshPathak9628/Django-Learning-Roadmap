# Django CRUD with Media Files - Project 17

This project shows how to build a simple user profile manager in Django. Users can add, view, edit, and delete profiles with images.

## Quick Notes

- **Goal**: CRUD operations (Create, Read, Update, Delete) with file uploads
- **Key Feature**: Handle text data and images together
- **Structure**: Use `core/` for settings, `base_app/` for logic, `templates/` for HTML

## What You Need

- Python 3.8+
- Django framework
- Basic knowledge of Django basics

## Step-by-Step Build Guide

### 1. Start Fresh

- Create a new folder for the project
- Open terminal in that folder

### 2. Create Django Project

- Run: `django-admin startproject core .`
- This makes the main project folder

### 3. Make the App

- Run: `python manage.py startapp base_app`
- This creates the app for user logic

### 4. Set Up Database Model

- Go to `base_app/models.py`
- Add fields: email, password, image (FileField), qualification
- Don't forget `__str__` method

### 5. Update Settings

- In `core/settings.py`:
  - Add 'base_app' to INSTALLED_APPS
  - Set MEDIA_URL and MEDIA_ROOT for file uploads
  - Add templates and static dirs

### 6. Create Views

- In `base_app/views.py`:
  - Make `index_view`: show all users, handle new user form
  - Make `edit_view`: update existing user, handle image changes
  - Use get_object_or_404 for safety

### 7. Set Up URLs

- In `core/urls.py`:
  - Import views from base_app
  - Add paths: '' for index, 'edit/<id>/' for edit
  - Add media serving for development

### 8. Make Templates

- Create `templates/` folder
- Make `index.html`: list users in cards, add form at bottom
- Make `edit.html`: form to edit user, show current image
- Use Bootstrap for nice styling

### 9. Run Database Setup

- Run: `python manage.py makemigrations`
- Run: `python manage.py migrate`

### 10. Test It

- Run: `python manage.py runserver`
- Open browser to http://127.0.0.1:8000/
- Add users, upload images, edit them

## Tips

- Always use `enctype="multipart/form-data"` in forms with files
- Check `request.FILES` for uploaded images
- Images save to `media/images/` folder
- Use `{{ user.image.url }}` in templates to show images

## Next Steps

- Add delete functionality
- Add user authentication
- Improve styling or add more features

That's the basic flow. Start with models, then views, then URLs, then templates.
class="form-control"
accept="image/\*"
/>
<small class="form-text text-muted"
            >Leave empty to keep current image</small
          >
</div>
<button type="submit" class="btn btn-primary">Update</button>
<a href="{% url 'index' %}" class="btn btn-secondary ms-2">Back</a>
</form>
</div>

  </body>
</html>
```

### 9. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 10. Start the Server

```
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## What This App Does

- Show all users in cards with their images
- Add new users with photos
- Edit existing users (change info or upload new image)
- Delete users (you can add this later)
- Images are saved in `media/images/`

That's it! Now you can build and run your own CRUD app with media files.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
How to Setup and Run
Environment Setup: Activate your virtual environment.

Clean Migrations: \* Delete db.sqlite3.

Run python manage.py makemigrations and python manage.py migrate.

Start Server: Run python manage.py runserver.

Testing CRUD: \* Fill the form on the Home Page to Create.

Click the Edit link to update the Email or Image.
