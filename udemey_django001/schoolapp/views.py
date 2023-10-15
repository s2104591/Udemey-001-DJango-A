from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView


def homeview(request):
    # note this this is the previous way
    return render(request, "schoolapp/homefunction.html") 


class HomeView(TemplateView):
    # note this this is the new way using templates instead of functions
    template_name="schoolapp/homeclass.html"

    pass
