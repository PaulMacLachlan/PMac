from django.shortcuts import render

# Create your views here.

def index(request):
    print "were in the index method"
    return render(request, 'game_of_thrones/index.html')
