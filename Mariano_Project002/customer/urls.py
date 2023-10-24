from django.urls import path 
from . import views 


app_name = 'customer'


urlpatterns = [
     # practice
     path("one", views.one, name='nm-001'),

     # create customer using Model Forms (really good but class based views even better)
     path("two", views.createcustomer, name='nm-createcustomer1'),
     
     # create customer using class Bassed Views (recommended)
     path("three", views.CustomerCreate.as_view(), name='nm-createcustomer2'),
     
     # thank you
     path("four", views.thankyou, name='nm-thankyou'),

      
]

