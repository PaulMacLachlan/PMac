from django.shortcuts import render, redirect

from . models import Course

# Create your views here.
def index(request):
    print "This is the index Route!"
    return render(request, "index.html")

def process(request):
    if request.method == "POST":
        things = request.POST
        print things
        print "This is the process route!"
        request.session['course_name'] = request.POST['name']
        print "and were FINISHED!"
        return render(request, "index.html", things)
    else:
        return redirect('/')
