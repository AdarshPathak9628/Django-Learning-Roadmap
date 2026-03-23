

Project 11: Django Model Forms (Professional Guide)

1. Project Overview
   The goal of this project was to move away from manual HTML forms and use Django ModelForms. Instead of writing every input tag ourselves, we told Django to look at our Database Table (Model) and generate the form automatically. This makes the code cleaner, faster, and more secure.

2. Key Implementation Steps
   Project Refactoring: Renamed the project to 11_Django_ModelForms and the app to base_app to follow professional naming standards.

Database Table (models.py): Created a Student model with fields for Name, Email, and Roll No.

Form Creation (forms.py): Created a new file called forms.py. By using forms.ModelForm, we linked the form directly to our Student model.

Business Logic (views.py): Handled two main scenarios:

GET Request: To display a blank form when the user visits the page.

POST Request: To validate the user's input and save it directly to the database using form.save().

Template Rendering (index.html): Used Bootstrap 5 to create a split-screen layout—one side for the entry form and the other for the data table.

3. Important Technical Notes
   CSRF Protection: Every form must include the {% csrf_token %} tag. This is a mandatory security feature in Django to prevent cross-site attacks.

Automatic Fields: Using {{ form.as_p }} allows Django to render all form fields automatically. You don't need to write <input> tags for every field.

Data Validation: ModelForms automatically check if the email format is correct or if required fields are left empty.

Redirection: After saving data, we used redirect('/'). This prevents the browser from resubmitting the form if the user refreshes the page.

Data Looping: Used a {% for %} loop in HTML to dynamically display all database records in a professional table format.

4. How to Run the Project
   Activate your virtual environment (.venv).

Run python manage.py makemigrations and migrate to sync the database.

Start the server using python manage.py runserver.

Visit http://127.0.0.1:8000/ to see the form and table in action.
