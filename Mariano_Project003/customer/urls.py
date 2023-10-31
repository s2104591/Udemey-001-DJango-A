from django.urls import path 
from . import views 

from django.contrib.auth import views as auth_views




app_name = 'customer'


urlpatterns = [

     
     # this is now home page since in main urls.py specify path('', RedirectView.as_view(url="customer/")), 
     # and in settings.py specify ligin-redirect to home page so after login go to home page 
     # which in turn come to here
     path("", views.one, name='nm-001'),
     path("restricted001", views.restricted001,name="nm-resttricted001"),
     
     #path('signup1/',views.SignUpView.as_view(),name="nm-signup"),
     path('register/',views.register,name="nm-signup"),
     path('logout/',views.Logout,name="nm-logout"),
     path('login/',views.Login,name="nm-login"),

     #path('login1/',views.Login,name="nm-login1"),
     #path('login2/',auth_views.LoginView.as_view(),name="nm-login2"),
     
     path("change-password/", auth_views.PasswordChangeView.as_view()),
     path("thankyou/", views.thankyou, name ="nm-thankyou"),


     # Project 003
     
     #path('profile/<int:pk>/',views.CustomerProfile,name='nm-customer-profile'),
     #path('profile/<int:pk>/',views.CustomerProfile,name='nm-customer-profile'),
     
     #path('profile/',views.CustomerProfile,name='nm-customer-profile'),
     #path('update/<int:pk>/',views.CustomerUpdate.as_view(),name='nm-customer-update'),
     #path('summary1/',views.customersummary1,name='nm-customer-summary1'),

     path('summary22/',views.CustomerSummary22.as_view(),name='nm-customer-summary22'),
     path('summary/<int:pk>',views.CustomerSummary22.as_view(),name='nm-customer-summary2'),
     path('summary1/',views.customersummary1,name='nm-customer-summary1'),







     
     


 
      
]

