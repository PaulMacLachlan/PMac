from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    timestamp = datetime.now()
    context = {
        'date': timestamp.strftime("%b %d, %Y"),
        'time': timestamp.strftime("%I: %M %p")
    }
    return render(request, 'timedisplay/index.html', context)

def show(request):
    print(request.method)
    # context = {
    # "somekey":"somevalue"
    # }
    return render(request, 'timedisplay/show.html')
