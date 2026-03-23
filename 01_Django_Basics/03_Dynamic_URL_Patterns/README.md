# Project 03: Dynamic URL Patterns Guide

In this project, we learned how to capture data directly from the browser URL.

### Step 1: Professional Setup

- Renamed project folder to 'core'.
- Renamed app folder to 'base_app'.

### Step 2: Dynamic Paths (urls.py)

We used Path Converters to make URLs flexible:

- `<str:username>`: Captures any word/text.
- `<int:roll_no>`: Captures any integer/number.

### Step 3: Function Logic (views.py)

The dynamic data from the URL is passed as an argument to our Python function.
Example: `def user_view(request, username):`

### How to Run:

1. `python manage.py runserver`
2. Test dynamic links:
   - http://127.0.0.1:8000/user/Adarsh/
   - http://127.0.0.1:8000/roll/22/
