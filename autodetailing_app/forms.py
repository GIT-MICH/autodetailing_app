from django import forms
from django.core.exceptions import ValidationError

from autodetailing_app.models import Service, Opinion


class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {'categories': forms.CheckboxSelectMultiple()}


class AddOpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = '__all__'
        widgets = {'user': forms.HiddenInput}
        labels = {'description': 'Opinia'}
