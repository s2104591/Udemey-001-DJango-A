# appcatalog



from django.urls import path 
from . import views 


urlpatterns = [
    path('',views.indexMine,name='index'),
    path('createbook/',views.BookCreate.as_view(),name='createbook'),
    path('book/<int:pk>/',views.BookDetail.as_view(),name='book_detail'),
    path('my_view',views.my_view,name='my_view'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('profile/',views.CheckedOutBooksByUserView.as_view(),name='profile') 
]
