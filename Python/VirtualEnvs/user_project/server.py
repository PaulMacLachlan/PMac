from flask import Flask, render_template, redirect, session, flash, request

import re

app = Flask(__name__)

app.secret_key = 'secretkey'

@app.route('/')
def index():
    return render_template('index.html') # localhost:5000/some_route

@app.route('/user')
def user():
    email_reg = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    name_reg = re.compile(r'[a-zA-Z]+')
    errors = False
    if not name_reg.match(request.form['first_name']):
        flash('Invalid First Name')
        errors = True

    if not name_reg.match(request.form['last_name']):
        flash('Invalid Last Name')
        errors = True

    if errors
    #redirect to flash

    input = {'session'}
    return render_template()

app.run(debug=True)
