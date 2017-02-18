from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    print request.session
    # context = {
    # 'first_name': request.POST('first_name'),
    # 'dojo_location': request.POST('dojo_location'),
    # 'fav_lang': request.POST('fav_lang'),
    # 'comments': request.POST('comments')
    # }
    return render(request, 'survey_form/index.html') #, context)

# def result(request):
#     response = "Hello World!"
#     print (request.method)
#     return render(request, 'survey_form/result.html')

def process(request):
    if request.method == 'POST':
        print ("$" * 10)
        print request.POST
        # print request.method
        return redirect('/result')
