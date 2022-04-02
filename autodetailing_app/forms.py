from django import forms
from django.core.exceptions import ValidationError

from autodetailing_app.models import Service, Opinion, Worker, Cart, Order


class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {'categories': forms.CheckboxSelectMultiple()}


class AddOpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        exclude = ['user', 'created']
        labels = {'description': 'Opinia'}


class AddWorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'
        labels = {'name': 'Imię i nazwisko'}


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        exclude = ['user', 'services']
        widgets = {
            'meeting_date': forms.SelectDateWidget()
        }
        labels = {
            'services': '',
            'worker': 'Pracownik',
            'meeting_date': 'Data realizacji'
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['user', 'services', 'created', 'is_done']
        widgets = {
            'meeting_date': forms.SelectDateWidget()
        }
        labels = {
            'services': '',
            'worker': 'Wybierz pracownika',
            'meeting_date': 'Data realizacji'
        }
