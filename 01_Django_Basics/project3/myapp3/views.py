from django.shortcuts import render

# Create your views here.

def test_views(request):
    data = {'name': 'iics', 'password': 1234}
    return render(request, 'test.html', data)
def test(request):
    return render(request,'test1.html')