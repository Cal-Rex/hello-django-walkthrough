from django.shortcuts import render, HttpResponse


# Create your views here.
def sey_hello(request):
    return HttpResponse("Hello!")
