Project 04: Django Templates & Data Rendering
This project teaches how to connect Python Logic with HTML Templates to create a dynamic Employee Management table.

Logic Mind Map
Request: User types /info/ in the browser.

URL Mapping: core/urls.py -> base_app/urls.py.

View Logic: views.py prepares the data (List of Employee Dictionaries).

Context: The data is wrapped in a "Context Dictionary" and sent to the Template.

Template Rendering: info.html uses a {% for %} loop to draw the table.

Response: User sees a clean HTML table with employee details.

Structured Steps
Step 1: Folder Architecture
Root Folder: 04_Django_Templates_Basic

Settings Folder: core/ (Renamed from project4)

App Folder: base_app/ (Renamed from myapp4)

Template Folder: templates/ (Created in the root directory)

Step 2: Register & Configure Settings
File: core/settings.py

Add 'base_app' to the INSTALLED_APPS list.

Tell Django where the HTML files are by updating the TEMPLATES list:
'DIRS': [os.path.join(BASE_DIR, 'templates')],

Step 3: Define the Data (The Brain)
File: base_app/views.py

We created a list of dictionaries containing eid, name, and salary.

We used render(request, 'info.html', data) to send this list to the front end.

Step 4: Design the HTML (The Look)
File: templates/info.html

We used a standard <table> tag.

DTL (Django Template Language):

{{ variable_name }}: To print single values.

{% for emp in employees %}: To loop through the list and create rows.

{{ emp.name|title }}: A filter to capitalize the first letter of the name.

Step 5: Connect the Routes (The Map)
File: base_app/urls.py

Defined the path: path('info/', views.info_view, name='employee_info').

How to Run & Verify
Activate Environment: .\venv\Scripts\activate

Start Server: python manage.py runserver

Check Output: Open http://127.0.0.1:8000/info/

Key Professional Terms:
Context: The dictionary used to pass data from Python to HTML.

Rendering: The process of converting Django code into final HTML for the browser.

Template Tags: Code inside {% %} (Logic like loops/if-conditions).

Template Variables: Code inside {{ }} (Actual data values).
