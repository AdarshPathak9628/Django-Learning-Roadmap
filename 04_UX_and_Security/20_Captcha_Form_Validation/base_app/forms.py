from django import forms
from .models import student
from captcha.fields import CaptchaField

class StudentForm(forms.ModelForm):
    # Password input hides typed text in the browser.
    spaas = forms.CharField(
        max_length=100,
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    # Captcha stops simple bot submissions.
    captcha = CaptchaField()
    
    class Meta:
        model = student
        fields = ['name', 'phone', 'spaas', 'captcha']
        labels = {
            'name': 'Student Name',
            'phone': 'Contact'
        }
