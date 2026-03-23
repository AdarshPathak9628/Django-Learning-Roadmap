## Project 07: CRUD Basics (Part 1 - Database & Read)

In this project, we learned how to use Django Models to create a database table and how to display that data on a website.

### 1. Project Folder Structure (Tree View)

Plaintext
07_CRUD_Basics/
├── manage.py # The main file to run commands
├── db.sqlite3 # The actual Database file
├── core/ # Project Settings Folder
│ ├── settings.py # Registered 'base_app' here
│ └── urls.py # Main URL routing (Admin + App)
├── base_app/ # Application Logic Folder
│ ├── migrations/ # History of database changes
│ ├── templates/ # HTML Folder
│ │ └── home.html # Table to display Student data
│ ├── admin.py # Registered Student model for Admin Panel
│ ├── models.py # Defined the Student Table structure
│ ├── views.py # Logic to get data from Database
│ └── urls.py # Local App routes

### 2. Step-by-Step Implementation

Step 1: Creating the Model

We created a Student class in base_app/models.py.

We added fields: name (Text), roll_no (Number), and email (Email).

We added the **str** function so the Admin panel shows the Student Name instead of "Object 1".

Step 2: Database Migrations

python manage.py makemigrations base_app: Created a "Blueprint" of the table.

python manage.py migrate: Actually created the base_app_student table in the database.

Step 3: Admin & Superuser

python manage.py createsuperuser: Created a "Boss" account to manage data.

admin.py: Registered the model so we can add students using the browser.

Step 4: The "Read" Logic (Fetching Data)

Views: Used Student.objects.all() to pull all data from the database.

Templates: Used a {% for %} loop to show each student in a clean HTML Table.

### 3. Key Learning Points (Easy English)

Models: These are the "Blueprints" for your database. You define columns here.

Migrations: This is the "Bridge" that connects your Python code to the Database file.

Querysets: Student.objects.all() is like saying "Give me every row from the Student table."

Context: The dictionary {'students': all_students} is used to "pass" data from the Python file to the HTML file.

### 4. Common Errors We Fixed

OperationalError (No such table): Fixed by running the migrate command.

NameError (admin not defined): Fixed by adding from django.contrib import admin in urls.py.

Indentation Error: Learned that def **str** must be inside the class (4 spaces in).
