# 21 Email With Attachment

## Project Overview

This Django project shows how to send an email with a file attachment.
When the user clicks the **send email** link, Django sends an email to a fixed receiver email address and also attaches the `userr.txt` file.

This project is useful for learning:

- how to configure email in Django
- how to use SMTP with Gmail
- how to send an email from a Django view
- how to attach a file in email
- how to show a success message after sending


## Project Structure

- `core/`
  Main Django project settings, urls, asgi, and wsgi files
- `base_app/`
  App logic like views and app config
- `templates/`
  HTML page files
- `userr.txt`
  File that is attached in the email
- `manage.py`
  Main Django command file


## Main Features

- Send email from Django
- Attach a text file in the email
- Use Gmail SMTP settings
- Show success message on the page
- Print receiver email and message in terminal


## Tools and Modules Used

- `render()`
  Used to open and show the HTML page
- `redirect()`
  Used to send the user back to the home page after email is sent
- `EmailMessage`
  Used to create an email with more control
- `attach_file()`
  Used to attach a file with the email
- `send()`
  Used to send the final email
- `messages.success()`
  Used to show a success message in the browser
- `settings`
  Used to read email configuration from `core/settings.py`


## Step By Step Project Creation

### 1. Create Project Folder

Make a new folder for the project and open it in VS Code or terminal.


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

This command creates the main Django project files.


### 6. Create Django App

```powershell
python manage.py startapp base_app
```

This command creates the app where we write the project logic.


### 7. Add App In Settings

Open `core/settings.py` and add `base_app` inside `INSTALLED_APPS`.


### 8. Create Templates Folder

Create a folder named `templates` in the main project folder.

Then add this in `core/settings.py`:

```python
'DIRS': ['TEMPLATES'],
```

This tells Django where HTML files are stored.


### 9. Configure Email Settings

In `core/settings.py`, add:

```python
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_HOST_USER='your_email@gmail.com'
EMAIL_HOST_PASSWORD='your_app_password'
```

Important notes:

- `EMAIL_HOST` tells Django which mail server to use
- `EMAIL_PORT=587` is used for TLS
- `EMAIL_USE_TLS=True` makes email sending secure
- `EMAIL_HOST_USER` is the sender email
- `EMAIL_HOST_PASSWORD` should be a Gmail app password, not normal Gmail password


### 10. Create Email View

In `base_app/views.py`, make a function that:

- creates subject
- creates message
- gets sender email from settings
- sets receiver email list
- creates file path
- creates `EmailMessage`
- attaches file
- sends email
- shows success message
- redirects to home page


### 11. Create URL Paths

In `core/urls.py`, add:

- one URL for home page
- one URL for sending email

Example:

```python
path('send_email/', views.send_email, name='send_email')
path('', views.index)
```


### 12. Create HTML File

In `templates/index.html`, add a simple link or button:

```html
<a href="{% url 'send_email' %}">send email</a>
```

This will call the email sending view.


### 13. Add Attachment File

Create a file named `userr.txt` in the main project folder.

This file will be attached with the email.


### 14. Run Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

In this project, `makemigrations` may show `No changes detected`, and that is okay.


### 15. Run Server

```powershell
python manage.py runserver
```


## How This Project Works

### When Home Page Opens

- Django loads `index.html`
- user sees the **send email** link


### When User Clicks Send Email

- `send_email()` function runs
- subject is created
- message text is created
- sender email is taken from settings
- receiver email is taken from `recipient_list`
- `userr.txt` file path is prepared
- `EmailMessage` object is created
- file is attached
- email is sent
- terminal prints email details
- browser shows success message
- page redirects back to home page


## Current Email Data In This Project

- Sender email comes from `EMAIL_HOST_USER`
- Receiver email comes from `recipient_list` inside `base_app/views.py`
- Message body is:
  `your otp is ....and dont share this otp`
- Attached file is:
  `userr.txt`


## Important Commands

### Activate Environment

```powershell
.venv\Scripts\Activate.ps1
```


### Go To Project Folder

```powershell
cd E:\Python-Web-Development\04_UX_and_Security\21_Email_With_Attachment
```


### Run Server

```powershell
python manage.py runserver
```


### Apply Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```


## Common Problems And Fixes

### 1. `manage.py` not found

Reason:
- You are in the wrong folder

Fix:

```powershell
cd E:\Python-Web-Development\04_UX_and_Security\21_Email_With_Attachment
python manage.py runserver
```


### 2. Email is not sending

Reason:

- wrong email password
- app password not used
- internet problem
- wrong SMTP settings

Fix:

- check `EMAIL_HOST`
- check `EMAIL_PORT`
- check `EMAIL_USE_TLS`
- use Gmail app password


### 3. Page redirects but no clear message

Fix:

- use `messages.success()` to show message
- use `print()` in terminal to see what was sent


## Learning Summary

In this project, you learned:

- how to create a Django project
- how to create a Django app
- how to connect urls and views
- how to configure Gmail SMTP
- how to send email using Django
- how to attach a file using `EmailMessage`
- how to show a success message after sending


## Final Run Steps

Follow these steps in order:

1. Open terminal in project folder
2. Activate virtual environment
3. Run `python manage.py migrate`
4. Run `python manage.py runserver`
5. Open browser
6. Open home page
7. Click **send email**
8. Check browser success message
9. Check terminal print output
10. Check receiver inbox
