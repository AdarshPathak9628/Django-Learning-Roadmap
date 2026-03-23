# Project 02: Multiple Views Logic

This project shows how to manage different pages like Home, About, and Contact.

Step 1: Internal Name

- Changed app name to 'base_app' in apps.py.

Step 2: Logic Layer

- Created 3 functions in views.py (home, about, contact).

Step 3: Routing Layer

- Main urls.py connects to base_app/urls.py.
- App urls.py maps paths to the correct functions.

How to Run:

1. python manage.py runserver
2. Visit /about/ and /contact/ in the browser.
