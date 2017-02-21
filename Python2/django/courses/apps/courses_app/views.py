from django.shortcuts import render

from . models import Course

# Create your views here.
def index(request):
    print "This is the index Route!"
    return render(request, "index.html")
