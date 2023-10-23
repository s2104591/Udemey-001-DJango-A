from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from .forms import CustomerForm
from .models import Customer

# Create your views here.

def one(request):
    return HttpResponse("hello One")

def thankyou(request):
    return render(request, 'customer/thankyou.html') 


def createcustomer(request):
    if (request.method=='POST'):
        print("**  post request made")
        form = CustomerForm(request.POST) 
        message=""
        if form.is_valid():
            
            fname=request.POST['firstname']
            #request.POST['firstname']="changed name" # not allowed immutable
            
            
            print("** post request, form YES valid, firstname=", fname)

            count=Customer.objects.filter(firstname__iexact=fname).count()
            print("count of customers with this firstname=",count)
            
            fname=fname.strip().lower()
            count=Customer.objects.filter(firstname__iexact=fname).count()
            
            if count>=1:
                message="name already exists"
                return render (request,'customer/createcustomer.html', context= {'form':form,"message":message} )
                pass

            else:
                newcust=Customer(firstname=fname )
                print("new customer, firstname=", newcust.firstname, len(newcust.firstname) )
                return redirect(reverse("customer:nm-thankyou" ))

            pass
        else:
            print("** post request, form NOT valid")


        pass
    else:
        print("**  non post  Request made")
        form = CustomerForm()
        return render (request,'customer/createcustomer.html', context= {'form':form,"message":"no message"} )
        pass


    
    pass



