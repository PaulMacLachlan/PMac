from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')


@app.route('/')
def index():
    query = "SELECT * FROM emails" # define your query
    email = mysql.query_db(query) # run query with query_db()
    print email # just for testing
    return render_template('index.html', email_address=email) # pass data to our template

@app.route('/emails', methods=['POST'])
def create():
    #this adds a friend to the database!
    data = {
        'email_address': request.form['email_address'],
    }
    query = "INSERT INTO emails (email_address, created_at, updated_at) VALUES (:email_address, NOW(), NOW())"

    print data;
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
