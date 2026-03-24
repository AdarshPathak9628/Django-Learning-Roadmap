# 22 Django User Authentication

## Project Overview

This Django project shows a simple user authentication system.
It allows a user to:

- sign up
- log in
- log out
- open a protected home page only after login

This project is useful for learning Django built-in authentication in an easy way.


## Project Structure

- `core/`
  Main Django project files like settings, urls, asgi, and wsgi
- `base_app/`
  App logic like views and app config
- `templates/`
  HTML pages for signup, login, home, and base layout
- `manage.py`
  Main Django command file


## Main Features

- user signup
- user login
- user logout
- protected home page
- Django built-in auth forms
- session-based login system


## Important Django Functions Used

- `render()`
  Used to open an HTML page
- `redirect()`
  Used to move the user to another page
- `UserCreationForm`
  Django built-in form for new user signup
- `AuthenticationForm`
  Django built-in form for user login
- `authenticate()`
  Checks if username and password are correct
- `login()`
  Creates login session for the user
- `logout()`
  Ends the current user session
- `login_required`
  Stops non-logged-in users from opening protected pages


## Step By Step Project Creation

### 1. Create Project Folder

Create a new folder and open it in terminal or VS Code.


### 2. Create Virtual Environment

```powershell
python -m venv .venv
```


### 3. Activate Virtual Environment

```powershell
.venv\Scripts\Activate.ps1
```


### 4. Install Django

```powershell
pip install django
```


### 5. Create Django Project

```powershell
django-admin startproject core .
```

This creates the main Django project.


### 6. Create Django App

```powershell
python manage.py startapp base_app
```

This app stores the authentication logic.


### 7. Add App In Settings

Open `core/settings.py` and add `base_app` inside `INSTALLED_APPS`.


### 8. Create Templates Folder

Create a folder named `templates`.

Then add this in `core/settings.py`:

```python
'DIRS': ['TEMPLATES'],
```

This tells Django where the HTML files are stored.


### 9. Create Authentication Views

In `base_app/views.py`, create these functions:

- `home()`
- `login_view()`
- `signup()`
- `logout_view()`

These functions handle the full auth flow.


### 10. Protect Home Page

Use:

```python
@login_required(login_url='login')
```

This means only logged-in users can open the home page.
If the user is not logged in, Django sends them to the login page.


### 11. Create URLs

In `core/urls.py`, add:

```python
path('', views.home, name='home')
path('login/', views.login_view, name='login')
path('signup/', views.signup, name='signup')
path('logout/', views.logout_view, name='logout')
```


### 12. Create HTML Templates

Create these files inside `templates/`:

- `base.html`
- `home.html`
- `login.html`
- `signup.html`


### 13. Use Django Built-In Forms

For signup:

```python
UserCreationForm
```

For login:

```python
AuthenticationForm
```

These forms save time because Django already provides them.


### 14. Run Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

In this project, `makemigrations` may show `No changes detected`, and that is normal because no custom model is added.


### 15. Run Server

```powershell
python manage.py runserver
```


## How This Project Works

### Signup Flow

1. User opens signup page
2. User fills username and password
3. `UserCreationForm` validates data
4. New user is saved
5. User is logged in automatically
6. User is redirected to home page


### Login Flow

1. User opens login page
2. User enters username and password
3. `AuthenticationForm` validates data
4. `authenticate()` checks the user credentials
5. `login()` creates user session
6. User is redirected to home page


### Logout Flow

1. User clicks logout
2. `logout()` clears the user session
3. User is redirected to login page


### Protected Home Page Flow

1. User opens home page
2. `login_required` checks session
3. If logged in, home page opens
4. If not logged in, user goes to login page


## Files Used In This Project

### `base_app/views.py`

This file contains:

- signup logic
- login logic
- logout logic
- protected home logic


### `core/urls.py`

This file connects the browser URLs with the view functions.


### `core/settings.py`

This file contains:

- installed apps
- template settings
- database settings
- middleware


### `templates/login.html`

This page shows login form.


### `templates/signup.html`

This page shows signup form.


### `templates/home.html`

This page is shown only after login.


## Important Commands

### Go To Project Folder

```powershell
cd E:\Python-Web-Development\04_UX_and_Security\22_Django_User_Authentication
```


### Activate Environment

```powershell
.venv\Scripts\Activate.ps1
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

### 1. `manage.py` not found

Reason:
- you are in the wrong folder

Fix:

```powershell
cd E:\Python-Web-Development\04_UX_and_Security\22_Django_User_Authentication
python manage.py runserver
```


### 2. Login page not opening

Reason:
- wrong url
- server not running

Fix:

- check `core/urls.py`
- run the server again


### 3. User cannot access home page

Reason:
- user is not logged in

Fix:

- login first
- then open home page


### 4. Signup works but login not working

Reason:

- wrong username
- wrong password

Fix:

- use the correct username
- use the same password used at signup


## Learning Summary

In this project, you learned:

- how to create a Django auth project
- how to use Django built-in forms
- how to sign up a user
- how to log in a user
- how to log out a user
- how to protect a page using `login_required`
- how Django sessions work in a basic auth system


## Final Run Steps

Follow these steps in order:

1. Open terminal in project folder
2. Activate virtual environment
3. Run `python manage.py migrate`
4. Run `python manage.py runserver`
5. Open browser
6. Open signup page
7. Create a new account
8. Login with the same account
9. Open home page
10. Test logout
