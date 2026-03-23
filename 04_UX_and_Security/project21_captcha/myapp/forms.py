from django import forms
from .models import student
from captcha.fields import CaptchaField

class StudentForm(forms.ModelForm):
    
    spaas = forms.CharField(
        max_length=100,
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    captcha = CaptchaField()
    
    class Meta:
        model = student
        fields = ['name', 'phone', 'spaas', 'captcha']
        labels = {
            'name': 'Student Name',
            'phone': 'Contact'
        }
