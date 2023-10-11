from django.urls import path
from . import views


app_name="myapp"

urlpatterns=[
    
    path("lessons",views.lessons),
    path("variablea",views.variableA, name="nm-variablea"),
    path("inheritence",views.inheritence, name="nm-inheritence"),
    path("errorexample",views.errorexample, name="nm-errorexample"),
    path("staticegg",views.staticegg, name="nm-staticegg"),
    path("databaseegg",views.databaseegg, name="nm-databaseegg"),
    path("carsite",views.carsite, name="nm-carsite"),




    
    
    path("htmlA",views.html_001),
    path("htmlB",views.html_002),
   

    

    path("home",views.index,name="index"),

   
   
    path("<int:no1>/<int:no2>",views.functparam,name="add"),
    
    # important: "news-number" need to come before "news-topic", otherwise will be treated as a string arguement
    # for example http://127.0.0.1:8000/myapp/1  , the 1 will be passed to news-number, but only 
    # will be passed as a string arguement (wrong) to news-topic if news-topic is first 

    path("<int:pageno>",views.newsarticle_pageno,name="news-number"),
    path("<str:the_topic>",views.newsarticle_topic,name="news-topic"),


    
    


]


   

  
   
    


