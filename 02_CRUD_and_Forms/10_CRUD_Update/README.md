## Project 10: CRUD - Update (Editing Database Data)

Is project mein humne seekha ki kaise pehle se save kiye gaye data ko fetch karke use Edit aur Update karte hain.

### 1. Project Folder Structure (Tree View)

Plaintext
10_CRUD_Update/
├── manage.py # Commands chalane ke liye
├── db.sqlite3 # Aapka Database
├── core/ # Main Settings
│ ├── settings.py # App register kiya
│ └── urls.py # Update URL connect kiya
├── base_app/ # App Logic
│ ├── templates/  
│ │ ├── home.html # Student List + Edit Button
│ │ └── update.html # Form jisme purana data dikhega
│ ├── models.py # Student Table
│ ├── views.py # Update Logic (Get + Post)
│ └── admin.py # Admin panel registration

### 2. Step-by-Step Implementation

Step 1: The Model & Admin

models.py mein Student table banayi.

admin.py mein admin.site.register(Student) likha taaki dashboard par data dikhe.

Step 2: The Update URL (urls.py)

Humne ek special URL banaya: path('update/<int:id>/', ...)

Why? Taaki Django ko pata chale ki hum kis specific student (ID) ko edit karna chahte hain.

Step 3: The Update Logic (views.py)

Step A (Fetch): Pehle Student.objects.get(id=id) ka use karke purana data nikala.

Step B (Display): Use update.html par bheja taaki user purani details dekh sake.

Step C (Save): Jab user ne "Update" dabaya, toh student.save() command se naya data database mein overwrite kar diya.

Step 4: The Template (update.html)

Humne input box mein value="{{ student.name }}" ka use kiya.

Why? Taaki edit karte waqt box khali na dikhe, balki purana naam pehle se likha hua aaye.

### 3. Key Learning Points (Easy English)

objects.get(id=id): Ye command database mein se sirf ek (unique) record dhoondhti hai.

instance.save(): Jab data pehle se database mein ho aur hume sirf badlaw (changes) save karne hon, tab save() use hota hai.

value attribute: HTML input mein value ka use purana data "show" karne ke liye hota hai.

Two-Step Process: Update hamesha do baar chalta hai—pehli baar data dikhane ke liye (GET) aur doosri baar naya data save karne ke liye (POST).

### 4. Quick Recap of All CRUD Commands

C (Create): Student.objects.create()

R (Read): Student.objects.all()

U (Update): student.save()

D (Delete): student.delete()
