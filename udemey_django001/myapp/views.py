from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

topics={"sports": "the sport-page", "arts": "the arts-page"}


def index(request):
    return HttpResponse("Hello Mariano Rico, Udemey course start October 2023 " )



def functparam(request, no1,no2):
    sum=no1+no1
    result=f' {no1} + {no2} = {sum}'
    return HttpResponse(result)    

def newsarticle(request, the_topic):
    result= topics[the_topic]
    return HttpResponse(result) 

    




