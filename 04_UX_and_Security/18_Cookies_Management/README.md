# Django Cookies Management - Project 18

This project shows how to work with browser cookies in Django. Learn to set, get, and manage cookies for user preferences and data.

## Quick Notes

- **Goal**: Learn cookie handling in Django web applications
- **Key Feature**: Set and retrieve cookies for user data and preferences
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
- This creates the app for cookie logic

### 4. Set Up Settings

- In `core/settings.py`:
  - Add 'base_app' to INSTALLED_APPS
  - Set TEMPLATES DIRS to templates folder

### 5. Create Views

- In `base_app/views.py`:
  - Make `set_cookie`: sets a simple cookie
  - Make `get_cookie`: retrieves and displays cookie
  - Make `set_operation`: sets username and color from form
  - Make `get_operation`: displays username and applies background color

### 6. Set Up URLs

- In `core/urls.py`:
  - Import views from base_app
  - Add paths: '' for set, 'get/' for get, 'so/' for set operation, 'go/' for get operation

### 7. Make Templates

- Create `templates/` folder
- Make `set.html`: form to input username and color
- Make `get.html`: displays cookie data with colored background
- Use Bootstrap for nice styling

### 8. Test It

- Run: `python manage.py runserver`
- Open browser to http://127.0.0.1:8000/ (or any available port)
- Set cookies and see them retrieved

## What This App Does

- Set simple cookies with user data
- Set cookies from form input (username, color)
- Retrieve and display cookie values
- Apply background color from cookie
- Navigate between set and get operations

## Tips

- Cookies are stored in the browser
- Use `response.set_cookie()` to set cookies
- Use `request.COOKIES.get()` to retrieve cookies
- Cookies persist across browser sessions
- Always handle cases where cookies don't exist

## Next Steps

- Add cookie expiration times
- Implement cookie deletion
- Add more complex cookie data
- Learn about signed cookies for security
