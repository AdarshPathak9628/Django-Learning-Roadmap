# Django Learning Roadmap: Project 1-10 Review

This document contains the summary, definitions, and logic of the first 10 Django projects. Before moving to Batch 3, I am reviewing the foundation.

---

## Django Core Concepts (The "Big 4")

In Django, everything works in a cycle called **MVT (Model-View-Template)**. Here is what each file does:

1. **URL (urls.py) - "The Address Book"**
   - **Definition:** It maps the browser URL to a specific function in `views.py`.
   - **Why?** To tell Django: "If the user types `/about/`, open the About Page logic."

2. **View (views.py) - "The Brain"**
   - **Definition:** It is a Python function that takes a web request and returns a web response.
   - **Why?** To handle logic, calculate data, and decide which HTML file to show.

3. **Model (models.py) - "The Database Table"**
   - **Definition:** It defines the structure of your data in Python code.
   - **Why?** To save information permanently (like Student names or Roll numbers) without writing SQL.

4. **Template (.html) - "The Presentation"**
   - **Definition:** The visual layer that the user sees in the browser.
   - **Why?** To display data dynamically using Django Template Language (DTL).

---

## Detailed Project Breakdown (1 to 10)

### **Batch 1: Setup & Basic Routing (Projects 1-5)**

- **Focus:** Installation and App Structure.
- **Learning:** How to create a project, an app, and write the first `HttpResponse`.
- **Key Command:** `django-admin startproject` and `python manage.py startapp`.

### **Batch 2: Design, Static Files & Models (Projects 6-10)**

#### **Project 6: Template Inheritance**

- **Concept:** Creating a `master.html` (Base) and extending it in `home.html` or `about.html`.
- **Definition:** Using `{% extends %}` and `{% block %}` to avoid repeating code.
- **Why?** To keep the Navbar and Footer consistent across all pages.

#### **Project 7 & 8: Static Files & Professional UI**

- **Concept:** Linking CSS and Images (`ramji.jpg`, `banner.jpg`).
- **Definition:** Using `{% load static %}` to tell Django where the design files are.
- **Why?** To build a real-world looking website with styling and animations (AOS).

#### **Project 9: Dynamic Tables (Logic in Templates)**

- **Concept:** Sending a List of Dictionaries from `views.py` to `.html`.
- **Definition:** Using `{% for student in result %}` to auto-generate table rows.
- **Why?** To display 100s of data records automatically instead of writing 100 HTML tags.

#### **Project 10: Database Integration (Models)**

- **Concept:** Creating the first Database Table (`class student`).
- **Definition:** Using `models.IntegerField()` and `models.CharField()` to define data types.
- **Why?** To move from "Static Data" (Hardcoded) to "Dynamic Data" (Saved in Database).

---

## Local Testing Checklist (Before Batch 3)

- [ ] Virtual Environment active?
- [ ] `python manage.py makemigrations` (To prepare the table)
- [ ] `python manage.py migrate` (To create the table in DB)
- [ ] `python manage.py runserver` (To check the output)

---

**Status:** Reviewing Projects 1-10
**Next Goal:** Batch 3 (Forms & CRUD Operations)
