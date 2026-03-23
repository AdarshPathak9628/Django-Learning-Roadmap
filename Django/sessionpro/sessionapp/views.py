from django.shortcuts import render

def set_session(request):
    request.session['name'] = 'ramji'
    return render(request, 'session.html')

def counter(request):
    c=request.session.get('count',0)
    c=c+1
    request.session['count']=c
    return render(request,'counter.html',{'c':c})
