from django.shortcuts import render, redirect

from .models import Course

def index(request):
    #initial route, should display the form, take input from that form, and display the existing courses in the table below.
    context = {
    'courses': Course.objects.all(),
    }
    print "This is the index Route!"
    return render(request, "index.html", context)

# def process(request):
#     # if request.method == "POST":
#     print request.POST
#     print Course.objects.all()
#     print "This is the process route!"
#     print "and were FINISHED!"
#     return render(request, "index.html", context)


def create_course(request):
    #if request is POST, create a course
    context = {
    'courses': Course.objects.all(),
    'description': Course.objects.all(),
    }
    if request.method == "POST":
        Course.objects.create_course(request.POST['course_name'])
        Description.objects.add_description(request.POST['description'])
        return render(request, "index.html", context)
    else:
        return redirect('/')

#
# def confirm_delete(request):
#     print "NAME OF ENTRY WE WANT TO DELETE BASED ON NUMERIC ID TIED TO REMOVE BUTTON"
#     print "DESCRIPTION FORM SAME ITEM"
#     return render(request, "destroy.html")
#
# def no_delete(request):
#     return redirect('/')
#
# def yes_delete(request):
#     return redirect('/')


    # request.session['course_name'] = request.POST['name']
