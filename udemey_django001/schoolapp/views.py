from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView
from . import forms as fm



def homeview(request):
    # note this this is the previous way
    return render(request, "schoolapp/homefunction.html") 


class HomeView(TemplateView):
    # note this this is the new way using templates instead of functions
    template_name="schoolapp/homeclass.html"

    pass

class Thanks(TemplateView):
    template_name="schoolapp/thankyou.html"

class ContactForm(FormView):
    # note need to also crrate forms.py 
    form_class=fm.ContactForm
    template_name="schoolapp/contact.html"
    
    
    # either of :
    #success_url="/schoolapp/thanks/"
    success_url=reverse_lazy("schoolapp:nm-thanks")

    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("invalid", form['name'],form['message'])
        response = super().form_invalid(form)
        response
        
    

    pass
