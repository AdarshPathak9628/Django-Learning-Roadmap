# 23 Custom User Auth With Captcha

## Project Overview

This Django project shows a custom user authentication system with captcha protection.

In this project:

- user can sign up
- user can log in
- user can log out
- user can open a protected home page after login
- captcha is used on signup and login forms
- a custom user model is used instead of Django default user model

This project is useful when you want better control over the user model and also want basic bot protection.


## Project Structure

- `core/`
  Main Django project files like settings, urls, asgi, and wsgi
- `base_app/`
  App logic like views, forms, models, and app config
- `templates/`
  HTML pages for signup, login, and home
- `manage.py`
  Main Django command file


## Main Features

- custom user model
- signup form with captcha
- login form with captcha
- protected home page
- logout system
- Django built-in authentication support
- better form styling using widget tweaks


## Installed Packages And Why

### 1. `django-simple-captcha`

Why we need it:

- to show captcha image
- to stop simple bot form submissions
- to add extra security on signup and login forms

What it gives:

- `CaptchaField`
- captcha image generation
- captcha validation
- captcha refresh URL support


### 2. `django-widget-tweaks`

Why we need it:

- to style Django form fields directly inside template
- to add Bootstrap classes like `form-control`
- to keep templates simple and clean

What it gives:

- template filter like `add_class`
- easy form styling without editing every widget in Python code


### 3. Django Built-In Auth

This project also uses Django built-in authentication tools:

- `UserCreationForm`
- `AuthenticationForm`
- `login()`
- `logout()`
- `login_required`

Why they are useful:

- fast setup
- safe default auth system
- less manual code


## Important Django Functions Used

- `render()`
  Used to open an HTML page
- `redirect()`
  Used to move the user to another page
- `login()`
  Creates user session after login
- `logout()`
  Removes the current user session
- `login_required`
  Stops non-logged-in users from opening protected pages
- `CaptchaField`
  Adds captcha validation in forms
- `UserCreationForm`
  Built-in signup form
- `AuthenticationForm`
  Built-in login form


## Step By Step Project Creation

### 1. Create Project Folder

Make a new folder and open it in terminal.


### 2. Create Virtual Environment

```powershell
python -m venv .venv
```


### 3. Activate Virtual Environment

```powershell
.venv\Scripts\Activate.ps1
```


### 4. Install Required Packages

```powershell
pip install django
pip install django-simple-captcha
pip install django-widget-tweaks
```


### 5. Create Django Project

```powershell
django-admin startproject core .
```


### 6. Create Django App

```powershell
python manage.py startapp base_app
```


### 7. Add Apps In Settings

Open `core/settings.py` and add:

```python
'base_app',
'captcha',
'widget_tweaks',
```


### 8. Create Templates Folder

Create a folder named `templates`.

Then add this in `core/settings.py`:

```python
'DIRS': ['TEMPLATES'],
```


### 9. Create Custom User Model

In `base_app/models.py`, create:

```python
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
```

Why:

- default Django user is good, but custom user gives more control
- email can be made unique
- future fields can be added easily


### 10. Tell Django To Use Custom User

In `core/settings.py`, add:

```python
AUTH_USER_MODEL = 'base_app.CustomUser'
```

This is very important because it tells Django to use your custom model.


### 11. Create Forms

In `base_app/forms.py`, create:

- `SignupForm`
- `LoginForm`

Use:

- `UserCreationForm`
- `AuthenticationForm`
- `CaptchaField`

Why:

- signup becomes easy
- login becomes easy
- captcha adds protection


### 12. Create Views

In `base_app/views.py`, create:

- `signup_view()`
- `login_view()`
- `home_view()`
- `logout_view()`

These functions handle the auth flow.


### 13. Protect Home Page

Use:

```python
@login_required(login_url='/')
```

This means user must login before opening home page.


### 14. Create URL Patterns

In `core/urls.py`, add:

```python
path('captcha/', include('captcha.urls')),
path('signup/', views.signup_view, name='signup'),
path('', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('home/', views.home_view, name='home'),
```


### 15. Create Templates

Create these HTML files:

- `signup.html`
- `login.html`
- `home.html`

In signup and login templates, use:

```django
{% load widget_tweaks %}
```

Why:

- to add Bootstrap classes to form fields


### 16. Run Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```


### 17. Run Server

```powershell
python manage.py runserver
```


## How This Project Works

### Signup Flow

1. user opens signup page
2. user fills username, email, password, confirm password, and captcha
3. `SignupForm` validates all fields
4. if data is valid, user is saved
5. user is redirected to login page


### Login Flow

1. user opens login page
2. user enters username, password, and captcha
3. `LoginForm` validates login data
4. `form.get_user()` gets the authenticated user
5. `login()` creates user session
6. user is redirected to home page


### Home Page Flow

1. user opens `/home/`
2. `login_required` checks if user is logged in
3. if logged in, home page opens
4. if not logged in, user goes to login page


### Logout Flow

1. user clicks logout
2. `logout()` removes session
3. user goes back to login page


## File Purpose

### `base_app/models.py`

Stores the custom user model.


### `base_app/forms.py`

Stores signup and login forms with captcha.


### `base_app/views.py`

Handles signup, login, logout, and home page.


### `core/settings.py`

Stores app settings, template settings, and custom user setting.


### `core/urls.py`

Connects browser routes with views and captcha URLs.


## Important Commands

### Go To Project Folder

```powershell
cd E:\Python-Web-Development\04_UX_and_Security\23_Custom_User_Auth_With_Captcha
```


### Activate Environment

```powershell
E:\Python-Web-Development\.venv\Scripts\Activate.ps1
```


### Install Required Packages

```powershell
pip install django-simple-captcha
pip install django-widget-tweaks
```


### Apply Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```


### Run Server

```powershell
python manage.py runserver
```


## Common Problems And Fixes

### 1. `No module named 'widget_tweaks'`

Reason:

- package is not installed in the active environment

Fix:

```powershell
pip install django-widget-tweaks
```


### 2. `No module named 'captcha'`

Reason:

- captcha package is not installed

Fix:

```powershell
pip install django-simple-captcha
```


### 3. Home page is not opening

Reason:

- user is not logged in

Fix:

- login first
- then open `/home/`


### 4. Signup or login form shows captcha error

Reason:

- wrong captcha entered

Fix:

- enter the captcha exactly as shown


## Learning Summary

In this project, you learned:

- how to use a custom user model
- how to use Django auth with custom forms
- how to add captcha in signup and login
- how to protect a page using `login_required`
- how to use widget tweaks in template
- how to manage auth flow in Django


## Final Run Steps

Follow these steps in order:

1. open terminal
2. go to project folder
3. activate virtual environment
4. run `python manage.py migrate`
5. run `python manage.py runserver`
6. open browser
7. open signup page
8. create a new account
9. login with captcha
10. open home page
11. test logout
