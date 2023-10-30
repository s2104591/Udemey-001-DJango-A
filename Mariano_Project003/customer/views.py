from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy, reverse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView,DetailView,ListView, UpdateView 
from django.forms import Textarea
from .models import Customer

from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect
from django.urls import reverse

#from .forms import CustomerForm, CustomerFormAll
#from .models import Customer

## ---------------------------------

def one(request):
    return HttpResponse("hello This is the Temporary Home Page for Customer")

@login_required
def restricted001(request):
    return render(request, 'customer/restricted001.html') 

class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name="customer/signup.html"

    pass

def Logout(request):
    #return redirect(reverse("customer:nm-logout" ))
    return redirect(reverse("logout" ))

def Login(request):
    return redirect(reverse("login" ))
    #return auth_views.LoginView.as_view()  # experiment

def thankyou(request):
    return render(request, 'customer/thankyou.html') 


# Project 003


def CustomerProfile(request,pk):
    
    profilecount= Customer.objects.filter(userID=pk).count()
    print("customer profile activated pk=", pk, "count=",profilecount)
    if profilecount==0:

        cust=Customer(userID=pk, preference1="none")
        cust.save()
        print("added profile")
        pass
    else:
        print("no profile added")



    #return CustomerUpdate.as_view() 
    #return HttpResponse("hello This is the Temporary Profile Page for Customer")
    #return redirect(reverse("nm-customer-update" ))
    return HttpResponseRedirect(f'/customer/update/{pk}/')
    pass


class CustomerUpdate(UpdateView):

        #form_class = CustomerFormAll 
        model=Customer
        fields ="__all__"  
        success_url= reverse_lazy("customer:nm-thankyou")
        template_name='customer/updatecustomer.html'


    




