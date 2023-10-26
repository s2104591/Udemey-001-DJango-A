from django.urls import path 
from . import views 


app_name = 'customer'


urlpatterns = [
     # practice
     path("one", views.one, name='nm-001'),

     # create customer using Model Forms (really good but class based views even better)
     path("two", views.createcustomer, name='nm-createcustomer1'),
     
     # create customer using class Bassed Views (recommended)
     path("register/", views.CustomerCreate.as_view(), name='nm-createcustomer2'),
     path("list/", views.CustomerList.as_view(), name='nm-customer-list'),
     path('update/<int:pk>/',views.CustomerUpdate.as_view(),name='nm-customer-update'),


     path('detail/<int:pk>/',views.CustomerDetail.as_view(),name='nm-customer-detail'),
 


     
     # thank you
     path("four", views.thankyou, name='nm-thankyou'),

      
]

