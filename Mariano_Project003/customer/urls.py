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
     path('signup/',views.SignUpView.as_view(),name="nm-signup"),
     path('logout/',views.Logout,name="nm-logout"),
     path('login1/',views.Login,name="nm-login"),
     path('login2/',auth_views.LoginView.as_view(),name="nm-login2"),



     
     


 
      
]

