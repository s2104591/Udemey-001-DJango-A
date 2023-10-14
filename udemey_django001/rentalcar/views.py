from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ReviewForm

#from django.shortcuts import render, redirect
#from django.urls import reverse


# Create your views here.
# example 
# return render(request, "carapp/addcar.html")    


def rental_thankyou(request):
    #return render(request, "rentalcar/bootstrap_compare.html") 
    return render(request, "rentalcar/thankyou.html")  
     

def rental_review(request):

    if request.method =="POST":
        form = ReviewForm(request.POST)
        param   =   {"form":form}
        if form.is_valid ():
            form.save()  # only is form is a  ModelForm
            print(form.cleaned_data)
            return redirect(reverse("rentalcar:nm-rental_thankyou") )
        else:
            return render(request, "rentalcar/review.html", context=param)
            pass




        pass
    else:
        form    =   ReviewForm()
        param   =   {"form":form}

        return render(request, "rentalcar/review.html", context=param)

        


      
