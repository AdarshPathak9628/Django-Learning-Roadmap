from django.shortcuts import render

# Create your views here.

# View to display all students in a simple table
def table(request):
    """Sends a list of students to the table template"""
    context = {'result': [
        {'srno': 1, 'roll': 101, 'name': 'adarsh', 'team': 'red'},
        {'srno': 2, 'roll': 102, 'name': 'pathak', 'team': 'blue'},
        {'srno': 3, 'roll': 103, 'name': 'utkasrh', 'team': 'green'},
        {'srno': 4, 'roll': 104, 'name': 'yash', 'team': 'red'},
        {'srno': 5, 'roll': 105, 'name': 'ananad', 'team': 'yellow'},
        {'srno': 6, 'roll': 106, 'name': 'harsh', 'team': 'green'},
        {'srno': 7, 'roll': 107, 'name': 'ishu', 'team': 'yellow'},
    ]}
    return render(request, "table.html", context)

# View to display students with even/odd row styling
def even_table(request):
    """Sends the same data to a template that uses cycle for styling"""
    context = {'result': [
        {'srno': 1, 'roll': 101, 'name': 'adarsh', 'team': 'red'},
        {'srno': 2, 'roll': 102, 'name': 'pathak', 'team': 'blue'},
        {'srno': 3, 'roll': 103, 'name': 'utkasrh', 'team': 'green'},
        {'srno': 4, 'roll': 104, 'name': 'yash', 'team': 'red'},
        {'srno': 5, 'roll': 105, 'name': 'ananad', 'team': 'yellow'},
        {'srno': 6, 'roll': 106, 'name': 'harsh', 'team': 'green'},
        {'srno': 7, 'roll': 107, 'name': 'ishu', 'team': 'yellow'},
    ]}
    return render(request, "even_table.html", context)