from django.urls import path
from . import views

app_name="schoolapp"

# path('school/', include("rentalcar.urls") ),

urlpatterns = [
    path("function/",views.homeview,name="nm-homeviewfunction"),
    path("",views.HomeView.as_view(),name="nm-homeviewclass"),
    path("thanks/",views.Thanks.as_view(),name="nm-thanks"),
    path("contact/",views.ContactForm.as_view(), name="nm-contact"),
    path("createteacher/", views.TeacherCreateView.as_view(),name="nm-createteacher") ,
    path("listteachers/", views.TeacherListView.as_view(),name="nm-listteachers") ,
    path("detail_teacher/<int:pk>", views.TeacherDetailView.as_view(),name="nm-detail-teacher") ,
                                    


    




    
]
