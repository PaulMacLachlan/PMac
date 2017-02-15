from django.shortcuts import render, HttpResponse
from datetime import datetime

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
