from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.template import RequestContext

# Create your views here.
#initial view, for /index.html, with the 'context' object and timestamp for getting the current time (in UTC for the moment:
def index(request):
    timestamp = datetime.now()
    context = {
        'date': timestamp.strftime("%b %d, %Y"),
        'time': timestamp.strftime("%I: %M %p")
    }
    return render(request, 'timedisplay/index.html', context)

#extra route for secondary, not required function, just for muscle memory:
def show(request):
    print(request.method)
    # context = {
    # "somekey":"somevalue"
    # }
    return render(request, 'timedisplay/show.html')



def create(request):
    request.session['name'] = request.POST['first_name']
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.method
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")
