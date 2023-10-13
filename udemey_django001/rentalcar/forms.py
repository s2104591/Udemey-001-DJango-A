from django import forms

class ReviewForm(forms.Form):
    firstname=forms.CharField(max_length=30 )
    surname=forms.CharField(max_length=30 )
    email=forms.EmailField(label="whats your email")
    review=forms.CharField(label="whats your review",max_length=30, 
    widget=forms.Textarea( attrs={'class':'dashedred','rows':"4",'cols':'40'} ))



