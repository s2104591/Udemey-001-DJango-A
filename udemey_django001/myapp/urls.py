from django.urls import path
from . import views




urlpatterns=[
    path("",views.index,name="index"),
    path("<int:no1>/<int:no2>",views.functparam,name="add"),
    path("<str:the_topic>",views.newsarticle,name="news"),


]