from django.shortcuts import render, HttpResponse
# CONTROLLER!!!

# Create your views here.

def index(request):
    response = "Hello, I am your first request!"
    print "Hello, I am your first request!","<--- this should be in your browser!"
    # response = "And I am another!"
    # print "And I am another!"
    return HttpResponse(response)


def index(request):
    print ("*"*100)
    return render(request, "first_app/index.html", )
