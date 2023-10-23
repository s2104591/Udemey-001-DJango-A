from django.urls import path 
from . import views 

app_name = 'customer'


urlpatterns = [
     path("one", views.one, name='nm-001'),
     path("two", views.createcustomer, name='nm-createcustomer'),
     path("three", views.thankyou, name='nm-thankyou'),
      
]

