from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(widget=forms.PasswordInput(), label='Hasło')


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Użyj conajmniej 8 znaków'}),
            'email': forms.EmailInput(attrs={'placeholder': 'kowalski@poczta.pl '})
        }
        help_texts = {
            'username': None,
        }


class UpdateUserPermissionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'user_permissions']
        widgets = {
            'user_permissions': forms.CheckboxSelectMultiple()
        }
