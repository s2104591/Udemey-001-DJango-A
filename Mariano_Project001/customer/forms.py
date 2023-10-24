from django import forms
from django.forms import ModelForm, Textarea


from .models import CustomerModel


class CustomerForm(ModelForm):
    class Meta:
        model= CustomerModel
        fields="__all__"
        #password = forms.CharField(widget=forms.PasswordInput)

        widgets = {
            "comments": Textarea(attrs={"cols": 20, "rows": 4, 'class':'dashedred'}),
            

        }    
        






