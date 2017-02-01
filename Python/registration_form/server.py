from flask import Flask, render_template, redirect, request, session, flash
import random, datetime, re
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe' #resets session if changed!
email_check = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)') # r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
password_check = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
@app.route('/', methods=['POST', 'GET'])
def index():
    #preset conditions:
    print "Were in the route function!"
    form_empty = False
    password_length = False
    password_match = False
    password_req = False

    if request.method == 'POST':
        print "were in the if statement!"
        inputs = request.values
        print inputs
        for value in inputs:
            if len(request.form[value]) == 0:
                form_empty = True
            if value == 'first_name' or value == 'last_name':
                if any (char.isdigit() for char in request.form[value]):
                    flash("Names cannot have numbers in them") #erring out 8 different times
                    # Discuss this logic w Garret
            # if value == 'password' or value == 'confirm':
            #     if len(request.form[value]) < 8:
            #         password_length = True
            #     if password_check.match(request.form[value]):
            #         pass
            #     else:
            #         password_req = True
            #     if request.form['password'] != request.form['confirm']:
            #         password_match = True
            # if value == 'email':
            #     if email_check.match(request.form[value]):
            #         pass
            #     else:
            #         flash("Please provide a valid e-mail address")
                    #if alls legit:
    if form_empty == True:
        flash('Please fill all necessary fields')
    if password_length == True:
        flash("Password must be at least 8 characters")
    if password_match == True:
        flash("Passwords must match")
    if password_req == True:
        flash("Password must contain one uppercase letter, one lowercase letter and one number")

    return render_template('index.html')
app.run(debug=True)
