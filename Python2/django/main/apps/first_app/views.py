from django.shortcuts import render

# Create your views here.

def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)
