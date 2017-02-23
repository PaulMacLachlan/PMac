from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

#index
def index(request):
    print "Running the index method, calling out to User."
    # user = User.userManager.login("me@codingdojo.com","Paul")
    # # DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
    # print (type(user))
    # print "User -->",User
    # print "user -->",user
    # if 'error' in user:
    #     pass
    # if 'theuser' in user:
    #     pass
    return render(request, "index.html")

#TODO# Routes Needed:

#register
def register(request):
    print "Running the register method!"
    errors = User.userManager.register(request.POST)
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
    if User.userManager.logout(request.session):
        messages.add_message(request, messages.SUCCESS, "Successfully logged out.")
    return redirect('/')

#login
def login(request):
    print "Running the login method!"
    user = User.userManager.login(request.POST)

    if user:
        request.session['user_id'] = user.id
        request.session['is_logged'] = True
        request.session['first_name'] = user.first_name
        messages.add_message(request, messages.SUCCESS, "Successfully logged in.")
    else:
        messages.add_message(request, messages.ERROR, "Invalid username / password.")

    return redirect('/success')

#success
def success(request):
    print "Running the success method!"
    return render(request, '/success.html')
