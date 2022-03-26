from django import forms
from django.core.exceptions import ValidationError

from autodetailing_app.models import Service, Opinion, Worker, Cart


class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {'categories': forms.CheckboxSelectMultiple()}


class AddOpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        exclude = ['user']
        labels = {'description': 'Opinia'}


class AddWorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'
        labels = {'name': 'Imię i nazwisko'}


class CartForm(forms.ModelForm):
    # service = forms.ModelChoiceField(queryset=Service.objects.all(), widget=forms.CheckboxSelectMultiple(), label='')
    # worker = forms.ModelChoiceField(queryset=Worker.objects.all(), label='Pracownik')
    # created = forms.DateField(widget=forms.SelectDateWidget(), label='Data realizacji usługi')
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