Project 05: Template Inheritance (Base Layout)

1. What is Template Inheritance?
   In simple terms, Template Inheritance is a way to create a "Master Layout" for your website. When building a site, most pages (like Home, About, and Contact) share the same Header, Navbar, and Footer. Instead of copying that code into every single HTML file, we create one main file called base.html. All other pages "borrow" the design from this file. This follows the DRY (Don't Repeat Yourself) principle in professional development.

2. Project Folder Structure
   We have organized the project using a professional naming convention:

Root Folder: 05_Template_Inheritance (The main project directory)

Core Folder: core (Contains global settings and main URL configurations)

App Folder: base_app (Contains your logic, views, and app-specific URLs)

Templates Folder: A central folder where all HTML files are stored.

3. Step-by-Step Development Process
   Step 1: Create the Master File (base.html)
   First, we created base.html. This file acts as the "Parent." We wrote the HTML skeleton here, including the Navbar and Footer. To tell Django where the unique content of other pages should go, we used Block Tags: {% block content %} ... {% endblock %}. This acts as a placeholder or an empty space.

Step 2: Create the Child Files (home.html, about.html, contect.html)
In these files, we do not write the full HTML structure.

We start the file with {% extends 'base.html' %}. This tells Django to copy the layout from the Master file.

We then put the specific information for that page (like "About Me" text) inside the {% block content %} section.

Step 3: Setup the View Logic
In views.py, we created three functions: home, about, and contect. Each function uses the render command to point to its specific HTML file. Even though the child files are small, Django combines them with the base file to show a full page.

Step 4: Configure the URL Routes
We mapped the URLs in urls.py. We created paths so that:

/ leads to the Home page.

/about/ leads to the About page.

/contect/ leads to the Contact page.

4. Important Rules to Remember
   The Extends Tag: This must always be the very first line of your child HTML file. If you put anything above it, Django will throw an error.

Matching Block Names: The name of the block in the child file must exactly match the name used in the parent file (e.g., if the parent uses 'content', the child must also use 'content').

Easy Updates: If you want to change the color of the Navbar, you only change it once in base.html, and it will automatically update on all other pages.

5. How to Run the Project
   Open your terminal and navigate to the 05_Template_Inheritance folder.

Activate your virtual environment (.venv).

Run the command: python manage.py runserver.

Open the browser and click the links in the Navbar to see the pages change while the Navbar stays the same.
