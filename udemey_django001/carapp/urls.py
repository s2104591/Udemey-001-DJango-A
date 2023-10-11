from django.urls import path
from . import views

app_name="carapp"

urlpatterns = [
    path("listcars/",views.listcars,name="nm-listcars"),
    path("deletecar/",views.deletecar,name="nm-deletecar"),
    path("addcar/",views.addcar,name="nm-addcar"),


    
]
