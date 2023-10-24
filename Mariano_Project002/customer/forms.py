from django import forms
from django.forms import ModelForm, Textarea


from .models import Customer



class CustomerForm(ModelForm):
    class Meta:
        model= Customer
        fields=["firstname",'password','passwordconfirm']

        widgets = {
            'password': forms.PasswordInput(),  # Use PasswordInput widget
            'passwordconfirm': forms.PasswordInput(),  # Use PasswordInput widget

        }


class CustomerFormAll(ModelForm):
    class Meta:
        model= Customer
        fields="__all__"
        #password = forms.CharField(widget=forms.PasswordInput)

        widgets = {
            "comments": Textarea(attrs={"cols": 20, "rows": 4, 'class':'dashedred'}),
            

        }    
        






