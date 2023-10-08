# Mariano, created myself

from django.shortcuts import render


def my_errorpage(request, exception):
    return render (request, "404.html", status=404)

    