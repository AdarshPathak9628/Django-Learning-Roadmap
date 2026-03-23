from django import forms

class myform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
