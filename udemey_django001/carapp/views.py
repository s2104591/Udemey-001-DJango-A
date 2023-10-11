from django.shortcuts import render, redirect
from django.urls import reverse

from .import models as m

# Create your views here.

def addcar(request):
    if request.POST:
        print("request made =",request.POST['model'] )
        m.Car.objects.create(model=request.POST['model'])
        print("car added")
        return redirect (reverse('carapp:nm-listcars'))
    else:    
        return render(request, "carapp/addcar.html")



def deletecar(request):
    if request.POST:
        id=request.POST['pk']
        print("deleting car",id)
        try:
            m.Car.objects.get(pk=id).delete()
            return redirect (reverse('carapp:nm-listcars'))
        except:
            print(id, "car not deleted")
            return redirect (reverse('carapp:nm-listcars'))   

        return render(request, "carapp/deletecar.html")

    else:
        return render(request, "carapp/deletecar.html")
    


def listcars(request):
    allcars= m.Car.objects.all();


    print("list- cars")
    return render(request, "carapp/listcars.html", context={'allcars':allcars})
