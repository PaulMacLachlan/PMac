from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')


@app.route('/')
def index():
    query = "SELECT * FROM friends" # define your query
    friends = mysql.query_db(query) # run query with query_db()
    print friends # just for testing
    return render_template('index.html', all_friends=friends) # pass data to our template

@app.route('/friends', methods=['POST'])
def create():
    #this adds a friend to the database!
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"

    print data;
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
