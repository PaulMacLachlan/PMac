from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "email": "blob@gmail.com",
        "name": "mike"
    }
    print context
    return render(request, "second_app/index.html", context)


def show(request, id):
    context = {
        "id": id
    }
    print context
    return render(request, "second_app/show.html", context)
