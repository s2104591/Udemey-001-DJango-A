from django.urls import path 
from . import views 


app_name = 'customer'


urlpatterns = [

     
     # this is now home page since in main urls.py specify path('', RedirectView.as_view(url="customer/")), 
     # and in settings.py specify ligin-redirect to home page so after login go to home page 
     # which in turn come to here
     path("", views.one, name='nm-001'),
     path("restricted001", views.restricted001,name="nm-resttricted001"),
     
     

     path("list", views.CustomerList.as_view(), name='nm-customer-list'),
  
     # create customer using Model Forms (really good but class based views even better)
     path("two", views.createcustomer, name='nm-createcustomer1'),
     
     # create customer using class Bassed Views (recommended)
     path("register/", views.CustomerCreate.as_view(), name='nm-createcustomer2'),
     path("list/", views.CustomerList.as_view(), name='nm-customer-list'),
     path('update/<int:pk>/',views.CustomerUpdate.as_view(),name='nm-customer-update'),


     path('detail/<int:pk>/',views.CustomerDetail.as_view(),name='nm-customer-detail'),
     path('signup/',views.SignUpView.as_view(),name="nm-signup"),
 


     
     # thank you
     path("four", views.thankyou, name='nm-thankyou'),

      
]

