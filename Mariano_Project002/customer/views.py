from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy, reverse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


from django.views.generic import CreateView,DetailView,ListView, UpdateView 
from django.forms import Textarea
from .models import Customer






from .forms import CustomerForm, CustomerFormAll
from .models import Customer

# Create your views here.

def one(request):
    return HttpResponse("hello This is the Home Page for Customer")

@login_required
def restricted001(request):
    return render(request, 'customer/restricted001.html') 


def thankyou(request):
    return render(request, 'customer/thankyou.html') 

def customer_exists(fname):
    fname=fname.strip().lower()
    count=Customer.objects.filter(firstname__iexact=fname).count()
    return count>=1



class CustomerUpdate(UpdateView):

        #form_class = CustomerFormAll 
        model=Customer
        fields ="__all__"  
        success_url= reverse_lazy("customer:nm-customer-list")
        template_name='customer/updatecustomer.html'




# method 1 of creating cutomer with validation - using Class Based Views 
# note only need to use 1 method, Classed Based Views recommended
class CustomerCreate(CreateView):
    #form_class = MyForm
    #form = CustomerForm(request.POST) 
    #form_class = CustomerForm

    # optional but recommended since allows greater control example text area for comments
    form_class = CustomerForm 

    #model= CustomerModel     # optional if specifying form_class, otherwise required
    #fields ="__all__"   # not allowed if specifying form_class, otherwise required


    success_url= reverse_lazy("customer:nm-thankyou")
    template_name='customer/createcustomer2.html'
    #failure_url = 'customer/sorry.html'

    def form_valid(self,form):    

        print("***  form valid print")    
        fname    = form.cleaned_data['firstname'].strip()
        password = form.cleaned_data['password'].strip()
        confirm  = form.cleaned_data['passwordconfirm'].strip()

         
        if customer_exists(fname):
            return self.render_to_response({'form': form,'message':f'{fname} already exists'})

        elif password != confirm:
            return self.render_to_response({'form': form,'message':'passwords do not match'})


        else:
            # this is where the form is passed into template
            print("super call form")
            return super().form_valid(form)
        
            #return super().form_invalid(form)
            

    pass



class CustomerList(ListView):
    #form_class = CustomerFormAll
    model=Customer
    queryset=Customer.objects.all()

    template_name="customer/customer_list.html"
    
    # if not showing change to default 
    # note by default="object_list"
    context_object_name="customerlist" 



class CustomerDetail(DetailView):
    model=Customer


class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name="customer/signup.html"

    pass


    



# method 2 of creating cutomer with validation - using Model Views
# note only need to use 1 method, Classed Based Views recommended . But Model Views still very good
def createcustomer(request):
    if (request.method=='POST'):
        print("**  post request made")
        form = CustomerForm(request.POST) 
        message=""
        if form.is_valid():
                        
            fname=request.POST['firstname']
            password=request.POST['password']
            passwordconfirm=request.POST['passwordconfirm']

            if customer_exists(fname):
                message=f"{fname} already exists  - 002"
                return render (request,'customer/createcustomer1.html', context= {'form':form,"message":message} )
            else:
                newcust=Customer(firstname=fname, password=password, passwordconfirm=passwordconfirm )
                newcust.save()
                print("new customer saved, firstname=", newcust.firstname, len(newcust.firstname) )
                return redirect(reverse("customer:nm-thankyou" ))

            pass
        else:
            print("** post request, form NOT valid")


        pass
    else:
        print("**  non post  Request made")
        form = CustomerForm()
        return render (request,'customer/createcustomer1.html', context= {'form':form,"message":"no message"} )
        


    
    pass



