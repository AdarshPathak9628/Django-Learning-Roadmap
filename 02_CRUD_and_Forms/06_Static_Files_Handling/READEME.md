## Project 06: The "Static Files" Master Guide

In this project, we moved from a boring "Text-only" website to a Professional Designed Website by adding CSS (Colors/Fonts) and Images.

### 1. Detailed Folder Structure (The Map)

Think of your project like a house. The core is the foundation (settings), the base_app is the room (logic), and static is the decoration (paint and photos).

core/: This is the "Brain." It tells Django where everything is located.

base_app/: This is the "Worker." It handles the logic (Views) and the pages (Templates).

static/: This is the "Storehouse." It holds files that don't change, like your CSS and Virat's photo.

manage.py: This is the "Key." You use it to start the engine (server).

### 2. Step-by-Step Breakdown (How we did it)

Step 1: The Settings Connection
Django doesn't know where your folders are by default. We went into core/settings.py and wrote:

STATIC_URL: This is the name used in the browser (e.g., 127.0.0.1:8000/static/).

STATICFILES_DIRS: This is the most important part. It tells Django: "Go look in the root folder for a folder named static."

Step 2: Organizing the Assets
We didn't just throw files everywhere. We were professional:

We put CSS in static/css/.

We put Images in static/images/.

Why? Because when you have 100 images, you want to find them easily!

Step 3: The "Magic" Template Tag
In our HTML, we used {% load static %} at the very top.

Think of it like an Import statement. Without this, Django will see {% static ... %} and think it is just normal text. Loading it turns on the "Static Engine."

Step 4: Linking the Photo
We used <img src="{% static 'images/virat.jpg' %}">.

Why not just write src="/static/images/virat.jpg"? Because if you change your folder name later, the {% static %} tag will automatically find the new path for you. It's "Smart Linking."

### 3. Key Concepts in Simple English

Concept Simple Explanation
Static Files Files that stay the same for every user (CSS, Images, JS).
{% load static %} The "Switch" that tells the HTML to start looking for CSS/Images.
base.html The "Parent" file. We put the CSS link here so every page gets the same design automatically.
Case Sensitivity If the file is virat.jpg, you cannot write Virat.jpg. Django is very strict!

### 4. Common Errors & How to Fix Them

"Image not showing?" -> Check if virat.jpg is spelled exactly the same in the folder and the code.

"CSS not working?" -> Make sure you restarted the server after changing settings.py.

"Template Syntax Error?" -> You probably forgot to put {% load static %} at the top of your HTML file.

### 5. Final Professional Result

By following this core and base_app pattern, your Project 06 is now Scalable. This means you can add 10 more apps to this project, and they can all share the same CSS and Images from the static folder.
