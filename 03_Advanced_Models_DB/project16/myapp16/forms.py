from django import forms

class Mylogin(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class Mysignup(forms.Form):
    eid=forms.CharField()
    name=forms.CharField()
    password=forms.CharField()
    email=forms.EmailField()
    
    
