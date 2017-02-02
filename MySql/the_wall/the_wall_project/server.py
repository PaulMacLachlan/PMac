from flask import Flask, session, render_template, redirect, flash

app = Flask(__name__)

app.secret_key = "SUPERSECRET"

@app.route('/', methods=['POST', 'GET'])
def index():
    #error if no input provided
    #registration page
    #take in user signin data
    #route it to db (POST)
    # query for db
    # return the username for header
    return render_template('index.html')

@app.route('/comments') #needs 'POST' method???
def commentPage(id): #takes an ID???
    #for displaying the comments page only?
    #has ability to reroute when new comments/messages update?
    return render_template('wall.html')

app.run(debug=True)
