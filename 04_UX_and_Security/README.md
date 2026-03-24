# 04 UX and Security

## Overview

This folder contains Django projects related to:

- user experience
- form handling
- media handling
- cookies
- captcha
- email
- authentication
- custom user system

This section starts from project `16` and goes up to project `23`.


## Total Projects

There are **8 projects** in this folder:

1. `16_Media_Files_Handling`
2. `17_CRUD_with_Media_Files`
3. `18_Cookies_Management`
4. `19_Django_ModelForm`
5. `20_Captcha_Form_Validation`
6. `21_Email_With_Attachment`
7. `22_Django_User_Authentication`
8. `23_Custom_User_Auth_With_Captcha`


## What You Learn Here

- how to upload and show media files
- how to do CRUD with images
- how to set and get cookies
- how to use Django ModelForm
- how to use captcha in forms
- how to send email with attachment
- how to build login and signup system
- how to use custom user model with captcha


## Project Summary

### 16 Media Files Handling

Learn how to:

- configure media settings
- upload files
- display uploaded images


### 17 CRUD With Media Files

Learn how to:

- create records
- update records
- delete records
- upload image with form data


### 18 Cookies Management

Learn how to:

- set cookies
- read cookies
- use cookies for simple user data


### 19 Django ModelForm

Learn how to:

- create form from model
- validate form
- save form data easily


### 20 Captcha Form Validation

Learn how to:

- add captcha in form
- validate form with captcha
- stop simple bot submissions


### 21 Email With Attachment

Learn how to:

- configure SMTP email
- send email from Django
- attach file in email


### 22 Django User Authentication

Learn how to:

- create signup page
- create login page
- logout user
- protect home page


### 23 Custom User Auth With Captcha

Learn how to:

- use custom user model
- add captcha in signup and login
- protect auth flow with extra validation


## How To Run Any Project

### 1. Go to project folder

Example:

```powershell
cd E:\Python-Web-Development\04_UX_and_Security\20_Captcha_Form_Validation
```


### 2. Activate virtual environment

```powershell
E:\Python-Web-Development\.venv\Scripts\Activate.ps1
```


### 3. Run migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```


### 4. Run server

```powershell
python manage.py runserver
```


## Notes

- some projects need extra packages like captcha or widget tweaks
- each advanced project has its own README with full notes
- root folder README is only a short guide
