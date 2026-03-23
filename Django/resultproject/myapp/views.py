from django.shortcuts import render

# Create your views here.

def result(request):
    return render(request,'result.html')

def final(request):
    return render(request,'final.html')

def max_view(request):
    return render(request,'max.html')



def calculate_marks(marks):
    max_mark = max(marks)
    min_mark = min(marks)
    avg_mark = sum(marks) / len(marks) if marks else 0  # Manually calculate average
    return max_mark, min_mark, avg_mark

def result_view(request):
    subjects = ['Maths', 'English', 'Hindi', 'Chemistry', 'Physics']
    marks_data = {
        'Maths': [90, 85, 95, 88],
        'English': [85, 82, 88, 86],
        'Hindi': [88, 84, 90, 87],
        'Chemistry': [92, 89, 94, 91],
        'Physics': [87, 85, 90, 88]
    } 

    selected_subject = request.GET.get('subject', 'Maths')
    marks = marks_data.get(selected_subject, [])

    max_mark, min_mark, avg_mark = calculate_marks(marks)

    context = {
        'subjects': subjects,
        'selected_subject': selected_subject,
        'max_mark': max_mark,
        'min_mark': min_mark,
        'avg_mark': avg_mark
    }
    return render(request, 'result_template.html', context)
