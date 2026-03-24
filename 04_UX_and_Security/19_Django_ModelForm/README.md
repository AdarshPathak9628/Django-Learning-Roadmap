# Django ModelForm - Project 19

This project demonstrates Django ModelForm usage for student registration. Learn how to create, validate, and save forms automatically.

## Quick Notes

- **Goal**: Learn Django ModelForm for automatic form generation and validation
- **Key Feature**: Student registration with name and phone fields
- **Structure**: Use `core/` for settings, `base_app/` for logic, `templates/` for HTML

## What You Need

- Python 3.8+
- Django framework
- Basic knowledge of Django models and forms

## Step-by-Step Build Guide

### 1. Start Fresh

- Create a new folder for the project
- Open terminal in that folder

### 2. Create Django Project

- Run: `django-admin startproject core .`
- This makes the main project folder

### 3. Make the App

- Run: `python manage.py startapp base_app`
- This creates the app for student logic

### 4. Set Up Database Model

- In `base_app/models.py`:
  - Create Student model with name and phone fields
  - Add proper field types and constraints

### 5. Create ModelForm

- In `base_app/forms.py`:
  - Create StudentForm class inheriting from ModelForm
  - Specify model and fields in Meta class

### 6. Update Settings

- In `core/settings.py`:
  - Add 'base_app' to INSTALLED_APPS
  - Set TEMPLATES DIRS to templates folder

### 7. Create Views

- In `base_app/views.py`:
  - Make index view to handle form submission
  - Validate form and save to database
  - Display all registered students

### 8. Set Up URLs

- In `core/urls.py`:
  - Import views from base_app
  - Add path for index view

### 9. Make Templates

- Create `templates/` folder
- Make `index.html`: form on left, student list on right
- Use Bootstrap for nice styling

### 10. Set Up Database & Run

**Create Migrations:**

```
python manage.py makemigrations
```

**Apply Migrations:**

```
python manage.py migrate
```

**Create Superuser (Optional - for admin panel):**

```
python manage.py createsuperuser
```

- Enter username, email, and password when prompted

**Start Development Server:**

```
python manage.py runserver
```

**Access the Application:**

- Open browser to: http://127.0.0.1:8000/
- Add students using the form and see them listed
- Access admin panel at: http://127.0.0.1:8000/admin/ (if superuser created)

## What This App Does

- Student registration form with validation
- Automatic form generation from model
- Save form data to database
- Display list of all registered students
- Bootstrap styled responsive interface

## Tips

- ModelForm automatically creates form fields from model
- Use `form.is_valid()` to validate input
- Call `form.save()` to save to database
- Access form fields individually with `form.field_name`
- ModelForm handles field types and validation automatically

## Next Steps

- Add form field customization
- Implement form editing and deletion
- Add form validation rules
- Create custom form widgets
