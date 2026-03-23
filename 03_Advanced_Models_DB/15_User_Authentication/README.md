Project 16: Professional User Authentication
Goal: To build a secure Signup, Login, and Logout system using Django’s built-in security features instead of manual models.

1. Core Concepts (Simple English)
   In this project, we stopped using our custom Emp_signup table and started using Django’s "Superhero" features:

User Model: A pre-built database table that handles usernames, emails, and passwords.

Password Hashing: Django never saves passwords as "12345". It converts them into a secret code (Hash) so even hackers cannot read them.

Session Management: When a user logs in, Django gives them a "Digital Token" (Session) so they stay logged in while browsing different pages.

2. The Professional Toolkit (Modules used)
   Tool Purpose
   UserCreationForm Automatically creates the Signup form with password validation rules.
   AuthenticationForm Handles the Login form and checks if the user exists.
   authenticate() Verifies if the Username and Password are correct.
   login() Starts the user's session (opens the door).
   logout() Ends the session (closes the door).
3. Key Code Logic
   The Signup Logic
   We use fm.save() which automatically handles everything:

Python
fm = UserCreationForm(request.POST)
if fm.is_valid():
fm.save() # Saves to the official 'auth_user' table
The Profile Logic (Template Tag)
To show the name of the person who is currently logged in, we use this simple tag in HTML:
Welcome, {{ request.user.username }}!

4. Why is this better than Project 15?
   High Security: Passwords are encrypted (Hashed).

Less Code: We don't have to write models.py for users; Django provides it.

Validation: It automatically checks if the password is too short or too common.

Admin Integration: All users created through your Signup page automatically appear in the Django Admin Panel (/admin).

5. Interview / Viva Questions for Adarsh:
   Q: What is the benefit of UserCreationForm?

Ans: It provides a ready-made signup form and handles password security automatically.

Q: Why do we use {% csrf_token %}?

Ans: It is a security shield that prevents "Cross-Site Request Forgery" (hackers submitting fake forms).

Q: How do we show the logged-in user's name?

Ans: By using the context variable {{ request.user }} in the template.
