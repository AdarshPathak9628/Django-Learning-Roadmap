## Project 08: CRUD - Create (Handling Web Forms)

In this project, we learned how to build a Web Form to collect user data and save it directly into the SQLite Database using Django’s POST method.

### 1. Project Folder Structure (Tree View)

Plaintext
08_CRUD_Create/
├── manage.py # Command-line utility
├── db.sqlite3 # Database storing our Students
├── core/ # Project Configuration
│ ├── settings.py # Registered 'base_app'
│ └── urls.py # Main URL routing
├── base_app/ # Application Logic
│ ├── templates/  
│ │ └── home.html # HTML Form + Data List
│ ├── models.py # Student Table Schema
│ ├── views.py # Logic to handle Form Submission
│ └── urls.py # Local routing

### 2. Step-by-Step Implementation

Step 1: The Model (Database Table)

We used the same Student model as Project 07.

This table has three columns: name, roll_no, and email.

Step 2: The HTML Form (home.html)

We created a <form> with method="POST".

Important: Each <input> must have a name attribute (e.g., name="s_name"). This is how Python identifies which box the data is coming from.

We added {% csrf_token %} inside the form for security.

Step 3: The View Logic (views.py)

We used if request.method == "POST": to separate the "showing the page" logic from the "saving the data" logic.

We used request.POST.get('name_here') to grab the user's typing.

We used Student.objects.create(...) to write a new row in the database.

Step 4: The Redirect

After saving, we used return redirect('/'). This clears the form and refreshes the page so the user can see their new entry immediately.

### 3. Key Concepts in Easy English

Concept Simple Explanation
method="POST" Used for sending sensitive data to the server (like passwords or new records).
{% csrf_token %} A secret code that prevents hackers from submitting fake forms on your site.
request.POST A dictionary-like object in Django that holds all the data submitted via a form.
objects.create() A shortcut command that both creates a Python object and saves it to the DB at once.
redirect() Tells the browser to go to a specific URL after an action is finished.

### 4. Common Troubleshooting for "Create"

403 Forbidden Error: This happens if you forget to put {% csrf_token %} inside your <form>.

Data Not Saving: Check if the name="..." attribute in your HTML matches the name inside request.POST.get('...') in your views.py.

Page Not Updating: Always use redirect() after a POST request to ensure the browser shows the latest data
