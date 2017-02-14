from django.shortcuts import render

# Create your views here.

def index(request):
    print "were in the index method"
    return render(request, 'game_of_thrones/index.html')

def process(request):
    if request.method == 'POST':
        print request.POST, "<--- HERE IS MY POST DATA"
        request.session['name'] = request.POST['name']
        return render(request, "index.html")

    else:
        print request.POST
        return redirect('/')

def sucess(request):
    pass
