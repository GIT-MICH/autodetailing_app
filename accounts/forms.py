from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(widget=forms.PasswordInput(), label='Hasło')