from django.urls import path
from . import views

app_name="rentalcar"

# path('rental/', include("rentalcar.urls") ),
# http://127.0.0.1:8000/rental/rental_review

urlpatterns = [
    path("rental_thankyou/",views.rental_thankyou,name="nm-rental_thankyou"),
    path("rental_review/",views.rental_review,name="nm-rental_review"),



    
]
