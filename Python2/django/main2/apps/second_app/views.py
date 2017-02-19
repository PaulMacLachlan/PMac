from django.shortcuts import render
from .models import People

# Create your views here.

def index(request):
    context = {
        "email": "fakeassemail@gmail.com",
        "name": "paul"
    }
    print context
    return render(request, "second_app/index.html", context)


def show(request, id):
    context = {
        "id": id
    }
    print context
    return render(request, "second_app/show.html", context)


#####
def index(request):
    People.objects.create(first_name="Paul",last_name="MacLachlan")
    people = Peopel.objects.all()
    print Peoplereturn render(request,"second_app/index.html")
