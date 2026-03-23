from django.shortcuts import render
from .models import Student

def index(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        q = request.POST.get('qualification')
        i = request.FILES.get('img')
        data = Student(name=n, email=e, age=a, gender=g, qualification=q, img=i)
        data.save()
    all_students = Student.objects.all()
    return render(request, 'index.html', {'all': all_students})

def edit_view(request,id):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        q = request.POST.get('qualification')
        i = request.FILES.get('img')
        data = Student(id=id, name=n, email=e, age=a, gender=g, qualification=q, img=i)
        data.save()
    all_students = Student.objects.get(id=id)
    return render(request, 'edit.html', {'all': all_students})


def delete_view(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        pass

    if request.method == "POST":
        student.delete()
        all_students = Student.objects.all()
        return render(request, 'index.html', {'all': all_students})

    return render(request, 'delete.html', {'stu': student})      
