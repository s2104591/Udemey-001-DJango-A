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
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import MySummaryForm, MySignForm

from django import forms

#from .models import Customer

## ---------------------------------

def one(request):
    return HttpResponse("hello This is the Temporary Home Page for Customer")

@login_required
def restricted001(request):
    return render(request, 'customer/restricted001.html') 


def Logout(request):
    #return redirect(reverse("customer:nm-logout" ))
    return redirect(reverse("logout" ))

def Login(request):
    return redirect(reverse("login" ))
    #return auth_views.LoginView.as_view()  # experiment

def thankyou(request):
    return render(request, 'customer/thankyou.html') 


# Project 003







def getCustomerAccount(uid, uname, email,fname,lname):
    profilecount= Customer.objects.filter(userID=uid).count()
    if profilecount==0:
        cust=Customer(userID=uid, userName=uname,preference1="none",email=email,firstname=fname,lastname=lname )
        cust.save()
        print("added customer account")
        pass
    else:
        cust=Customer.objects.get(userID=uid )
        if cust.userName=="?":
            cust.userName=uname
            cust.save()
        print("no account added since already exists")

    result=Customer.objects.get(userID=uid)    
    return result




class CustomerSummary22(LoginRequiredMixin ,UpdateView):
    
        model=Customer
        fields = "__all__"
        success_url= reverse_lazy("customer:nm-thankyou")
        template_name='customer/summary2.html'




class CustomerSummary22(LoginRequiredMixin ,UpdateView):

        form_class = MySummaryForm 
        #model=Customer
        #fields = ['preference1']
        success_url= reverse_lazy("customer:nm-logout")
        template_name='customer/summary22a.html'

        def get_initial(self):
            print("Update View Initial")

        def get_object(self, queryset=None):

            print("*** Update View getObject start")
            user_id = self.request.user.id
            user_name = self.request.user.username
            user_email= self.request.user.email
            user_firstname= self.request.user.first_name
            user_lastname= self.request.user.last_name

            ispost=self.request.POST
            print("ispost=",ispost)



            print("username,email=",user_name,user_email, user_firstname,user_lastname)
            cust=getCustomerAccount(user_id,user_name,user_email,user_firstname,user_lastname)    

           
            
            #obj = get_object_or_404(self.model, id=user_id)
            #print("*** Update View getObject",user_id)

            # Get the object to update based on the 'id' parameter in the URL
            #id = self.kwargs.get('id')
            

            #print("UpdateView get_Object, id =",id)
            return cust


def customersummary1(request):
    
    
    template= "customer/summary1.html"
    if request.method =="POST":
        form = MySummaryForm(request.POST)
        param   =   {"form":form}
        if form.is_valid ():
            form.save()  # only is form is a  ModelForm
            print(form.cleaned_data)
            return redirect(reverse("customer:nm-thankyou") )
        else:
            return render(request, template, context=param)       
    else:
        user_id     = request.user.id
        user_name   =""
        #user_name   = request.user_name
        print("userid",user_id, user_name)

        #cust=getCustomerAccount(user_id,user_name)


        form    =   MySummaryForm()
        param   =   {"form":form}

        return render(request, template, context=param)






##  ---------------------------  register note substitue for SignUp -- can take in email also 

def register(request):
    template_name="customer/signup.html"
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            fname=request.POST['first_name']
            sname=request.POST['last_name']
            uname=request.POST['username']
            
            print("register details=",email, fname, sname, uname)

            #user.emailaddress=email
            #user.firstname=fname
            #user.lastname=sname



            user = form.save()
          
        

            #login(request, user)
            #return redirect(reverse("login" ))
            return redirect(reverse("customer:nm-login" ))

    else:
        form = CustomUserCreationForm()
    return render(request, template_name, {'form': form})


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")
    first_name = forms.CharField(max_length=30, required=True, help_text="Enter your first name.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Enter your last name.")
    
 


    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')
    




