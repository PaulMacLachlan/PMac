from flask import Flask, render_template, redirect, request, session, flash
import random, datetime

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method['fname'] == 'garret':
        print type(request.method['fname'])
        print type('garret')
        flash('you suck put something besides garret')
    return render_template('index.html')

app.run(debug=True)