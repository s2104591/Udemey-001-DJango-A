from django import forms
from django.forms import ModelForm, Textarea


from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model= Customer
        fields="__all__"
        






