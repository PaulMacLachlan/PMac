from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
    "timetest": [1,2,3,4,5],
    "t2": "string"
    }
    return render(request, 'timedisplay/index.html')

def show(request):
    print(request.method)
    # context = {
    # "somekey":"somevalue"
    # }
    return render(request, 'timedisplay/show.html')
