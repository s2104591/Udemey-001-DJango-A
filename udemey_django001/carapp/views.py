from django.shortcuts import render

# Create your views here.

def addcar(request):
    return render(request, "carapp/addcar.html")



def deletecar(request):
    return render(request, "carapp/deletecar.html")
    


def listcars(request):
    print("list- cars")
    return render(request, "carapp/listcars.html")
