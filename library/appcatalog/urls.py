# appcatalog



from django.urls import path 
from . import views 


urlpatterns = [
    path('',views.index,name='index'),
    path('mine',views.indexMine,name='index'),
    path('createbook/',views.BookCreate.as_view(),name='createbook'),
    path('book/<int:pk>/',views.BookDetail.as_view(),name='book_detail'),
    path('requireslogin',views.requireslogin,name='nm-requireslogin'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('profile/',views.CheckedOutBooksByUserView.as_view(),name='profile') 
]
