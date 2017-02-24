from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

#index
def index(request):
    print "Running the index method, calling out to User."
    # user = User.objects.login("me@codingdojo.com","Paul")
    # # DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
    # print (type(user))
    # print "User -->",User
    # print "user -->",user
    # if 'error' in user:
    #     pass
    # if 'theuser' in user:
    #     pass
    return render(request, "index.html")



#register
def register(request):
    print "Running the register method!"
    errors = User.objects.register(request.POST)
    if errors:
        for error in errors:
            messages.add_message(request, messages.ERROR, error)
    else:
        messages.add_message(request, messages.SUCCESS, "User registered successfully.")
        return redirect('/success')

    return redirect('/')

#logout
def logout(request):
    print "Running the logout method!"
    if User.objects.logout(request.session):
        messages.add_message(request, messages.SUCCESS, "Successfully logged out.")
    return redirect('/')

#login
def login(request):
    print "Running the login method!"
    user = User.objects.login(request.POST)
    userName = request.session['first_name']
    if user:
        request.session['user_id'] = user.id
        request.session['is_logged'] = True
        request.session['first_name'] = user.first_name
        # userName = request.session['first_name']
        messages.add_message(request, messages.SUCCESS, "Successfully logged in.")
        print ("-"*10), messages
    else:
        messages.add_message(request, messages.ERROR, "Invalid username / password.")

    print ("-"*10), userName
    print ("-"*10), messages
    return redirect('/success', userName)

#success
def success(request):
    print "Running the success method!"
    return render(request, 'success.html')
