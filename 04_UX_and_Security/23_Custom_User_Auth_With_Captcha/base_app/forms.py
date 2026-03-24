from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField

class SignupForm(UserCreationForm):
    # EmailField checks that the entered value looks like an email.
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    # CaptchaField helps block simple bot submissions.
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'captcha']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }

class LoginForm(AuthenticationForm):
    # Captcha is also used on login for extra protection.
    captcha = CaptchaField()
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'captcha']
