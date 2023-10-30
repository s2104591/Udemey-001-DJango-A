from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy, reverse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView,DetailView,ListView, UpdateView 
from django.forms import Textarea
from .models import Customer

from django.contrib.auth import views as auth_views

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
    




