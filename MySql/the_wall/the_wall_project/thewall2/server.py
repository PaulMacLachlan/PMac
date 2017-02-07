from flask import Flask, session, redirect, render_template, flash, request
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'wall_2_database')
app.secret_key = "SECRETtopsecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # register user, insecure v1.0
    form = request.form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm']
    insert_query = "INSERT INTO users (first_name, last_name, email, password, confirm, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :confirm, NOW(), NOW())"
    query_data = { 'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password, 'confirm': confirm }
    mysql.query_db(insert_query, query_data)
    flash('passwords do not match!', 'errors')
    return render_template('wall.html')

# route for only signing in
@app.route('/login', methods=['POST'])
def login():
    return redirect('wall.html')

# route for signing out
@app.route('/logout', methods=['POST'])
def logout():
    session.pop
    return redirect('/')

@app.route('/wall')
def wall():
    return render_template('wall.html')

app.run(debug=True)
