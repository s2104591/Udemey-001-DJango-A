from django import forms
from django.forms import ModelForm, Textarea


from .models import RentalModel





#class ReviewForm(forms.Form):
#    firstname=forms.CharField(max_length=30 )
#   surname=forms.CharField(max_length=30 )
#    email=forms.EmailField(label="whats your email")
#    review=forms.CharField(label="whats your review",max_length=30) 
#    widget=forms.Textarea( attrs={'class':'dashedred','rows':"4",'cols':'40'} ))


class ReviewForm(ModelForm):
    class Meta:
        model=RentalModel
        fields=["firstname","surname",'rating',"comments"]
        labels={ "rating":"your rating"}

        widgets = {
            "comments": Textarea(attrs={"cols": 20, "rows": 4, 'class':'dashedred'}),
        }
        
        error_messages={
            'rating':{
                'min_value':'min value is 18',
                'max_value':'max value is 75',


            }
        }


    pass
