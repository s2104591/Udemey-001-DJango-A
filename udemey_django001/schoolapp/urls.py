from django.urls import path
from . import views

app_name="schoolapp"

# path('school/', include("rentalcar.urls") ),

urlpatterns = [
    path("function",views.homeview,name="nm-homeviewfunction"),
    path("",views.HomeView.as_view(),name="nm-homeviewclass"),
    




    
]
