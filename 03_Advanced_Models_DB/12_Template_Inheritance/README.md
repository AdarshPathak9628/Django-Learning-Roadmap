Project 12: Template Inheritance & App Refactoring

1. What is Template Inheritance?
   Instead of writing the same Bootstrap links, Header, and Footer on every page, we created one Master File (base.html). All other pages (like index.html) now "borrow" the design from the Master file. This makes the project much easier to manage.

2. Main Professional Steps
   App Renaming: We renamed the old project13 and myapp13 to core and pages_app. This involved updating manage.py, settings.py, urls.py, and admin.py to point to the new names.

The Master File (base.html): We put all the common code (HTML tags, Bootstrap CSS, and JS) here. We used {% block content %} to leave a placeholder for page-specific content.

The Child File (index.html): We used {% extends 'base.html' %} at the very top. This tells Django to use the Master design. We put our table inside {% block content %} to fill the placeholder.

Database Migration: Because we changed the App name, we ran makemigrations and migrate to create the new pages_app_employee table in SQLite.

3. Key Technical Points (Notes)
   {% extends %}: This must always be the first line in your child template.

{% block %} & {% endblock %}: These tags act like a "Start" and "Stop" sign for the content you want to inject into the Master file.

Project-Level Templates: We kept base.html in a global templates/ folder (set in settings.py) so it can be used by any app in the future.

Admin Panel: We used the Django Admin to add data, which instantly appeared in our Bootstrap table on the home page.

4. Summary of Files
   core/settings.py: Updated DIRS to include the project-level templates.

templates/base.html: The "Skeleton" or "Design" of the website.

pages_app/templates/index.html: The actual "Data" or "Body" of the home page.

pages_app/views.py: Fetches the Employee data and sends it to the template.
