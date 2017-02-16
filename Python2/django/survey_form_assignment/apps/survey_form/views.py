from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    # context = {
    # 'first_name': request.form('first_name'),
    # 'dojo_location': request.form('dojo_location'),
    # 'fav_lang': request.form('fav_lang'),
    # 'comments': request.form('comments')
    # }
    return render(request, 'survey_form/index.html') #, context)

def result(request):
    print (request.method)
    return render(request)
    return render(request, 'survey_form/result.html')

def process(request):
    if request.method == 'POST':
        print request.POST
        print request.method
        return redirect('/result')
