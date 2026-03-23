## Project 09: Full Setup (Migrations to Delete)

This guide covers everything we did, from setting up the database to deleting data.

### 1. Key Definitions (One-Line)

Models: The "Blueprint" or "Map" that tells Django how to create tables in the database.

Migrations: The "Bridge" that carries your Python model changes into the actual SQL database.

Admin Panel: A built-in "Dashboard" to manage (Add/Edit/Delete) your data without writing code.

Superuser: The "Master Account" or "Owner" who has full permission to access the Admin Panel.

Views: The "Brain" of your app that takes user requests and decides what data to show.

Urls: The "Address Book" that connects a web link (URL) to a specific Python function.

Runserver: The "Engine" that starts your local development environment.

### 2. Step-by-Step Implementation

Step 1: Folder & App Setup
We create the project structure and register our app so Django knows it exists.

django-admin startproject core .

python manage.py startapp base_app

Settings: Add 'base_app' to INSTALLED_APPS in settings.py.

Step 2: Creating the Model (models.py)
We define the Student table with Name, Roll No, and Email.

Why? To tell the computer exactly what kind of data we want to store.

Step 3: Migrations (Connecting to DB)
python manage.py makemigrations: Creates the plan.

python manage.py migrate: Executes the plan and creates the db.sqlite3 file.

Step 4: Superuser & Admin (admin.py)
python manage.py createsuperuser: Creates your login ID/Password.

admin.site.register(Student): Why? To make the Student table visible in the Dashboard.

Step 5: The Logic (views.py)
We wrote two functions:

Home View: To fetch all students using Student.objects.all().

Delete View: To find a student by ID and remove them using student.delete().

Step 6: Routing (urls.py)
We mapped the URLs.

path('', views.home): For the main page.

path('delete/<int:id>/', views.delete_student): Why? To tell Django which specific student ID to delete.

Step 7: The Frontend (home.html)
We created a table and used a {% for %} loop to display data.

We added a link: <a href="/delete/{{ s.id }}/">Delete</a>.

Step 8: Start the Engine
python manage.py runserver: To see the website live at http://127.0.0.1:8000/.

### 3. Why did we do this? (The Logic)

Why create a Model? Because without a Model, there is no place to save data permanently.

Why use Migrations? Because Databases don't understand Python code; Migrations translate Python into Database language.

Why register in Admin? So that you (the developer) can easily check if data is being saved correctly without opening the database file manually.
