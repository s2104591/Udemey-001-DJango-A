from django import forms
from django.forms import ModelForm, Textarea


from .models import Customer
from django.contrib.auth.models import User 





#class ReviewForm(forms.Form):
#    firstname=forms.CharField(max_length=30 )
#    surname=forms.CharField(max_length=30 )
#    email=forms.EmailField(label="whats your email")
#    review=forms.CharField(label="whats your review",max_length=30) 
#    widget=forms.Textarea( attrs={'class':'dashedred','rows':"4",'cols':'40'} ))

class MySignForm(ModelForm):
    class Meta:
        model = User 
        #fields = ['username','email','password']
        fields="__all__"



class MySummaryForm(ModelForm):
    class Meta:
        model=Customer
        #fields="__all__"
        fields=['userName','preference1']
        labels={ "preference1":"your 1st preference"}

    def __init__(self, *args, **kwargs):
        # Important , need to include all the fields specified in fields on the template, otherwise won't submit 
        # however can make them readonly or hidden as below
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['userName'].widget.attrs['readonly'] = True  
        self.fields['userName'].widget = forms.HiddenInput()  

    pass




