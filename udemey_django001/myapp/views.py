from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse




# Create your views here.

topics={"sports": "the sport-page", "arts": "the arts-page"}
the_topic_list = list(topics.keys())


def index(request):
    return HttpResponse("Hello Mariano Rico, Udemey course start October 2023 " )



def functparam(request, no1,no2):
    sum=no1+no1
    result=f' {no1} + {no2} = {sum}'
    return HttpResponse(result)    

def newsarticle_topic(request, the_topic):

    if topics.get(the_topic)==None:
        result= f"{the_topic} NOT FOUND. 404 Generic Error"
        
        #return HttpResponseNotFound(result)
        raise Http404(result)
    else:    
        result= topics[the_topic]

    return HttpResponse(result) 

def newsarticle_pageno(request, pageno):
    the_topic=the_topic_list[pageno]
    use_reverse=True

    if use_reverse:
        # alot more easier and clearer
        webpage=reverse('news-topic', args=[the_topic])
        return HttpResponseRedirect(webpage )

            
    return HttpResponseRedirect( the_topic  )


def html_001(request):
    # project level, not recommended , html in templates/myapp
    return render(request, "myapp/exampleA.html")
    pass

def html_002(request):
    # app level, ie html file in myapp/templates/myapp
    return render(request, "myapp/exampleB.html") 

def variableA(request):

    name={"firstname":"maRiano","surname":"riCo","scores":[90,70,60,100],'somedict':{"key" :"val"}}


    return render(request, "myapp/variableA.html",context=name)




    




