from django.shortcuts import render

# Create your views here.

def info(request):
    data={'details':[
        {'eid':101,'name':'adarsh','salary':30000},
        {'eid':102,'name':'pathak','salary':12000},
        {'eid':103,'name':'aditya','salary':55000},
        {'eid':104,'name':'tiwari','salary':60000},
        {'eid':105,'name':'utkarsh','salary':40000},
        {'eid':106,'name':'pathak','salary':20000},
        {'eid':107,'name':'virat','salary':3000}
    ]}
    return render(request,"info.html",data)