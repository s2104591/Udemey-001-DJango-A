from django.urls import path 
from . import views 


app_name = 'customer'


urlpatterns = [
     path("one", views.one, name='nm-001'),
     path("two", views.createcustomer, name='nm-createcustomer1'),
     path("three", views.CustomerCreate.as_view(), name='nm-createcustomer2'),
     path("four", views.thankyou, name='nm-thankyou'),

      
]

