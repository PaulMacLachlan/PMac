from flask import Flask, session, render_template, redirect, flash
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
# pw_hash = bcrypt.generate_password_hash('hunter2')
# bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True

#regex for email validation:
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app.secret_key = "SUPERSECRET"

from mysqlconnection import MySQLConnector
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'wall_database')
# an example of running a query
print mysql.query_db("SELECT * FROM users")

@app.route('/', methods=['POST', 'GET'])
def index():
    # the initial root index registration view.
    print session
    print "thats session!"
    #error if no input provided
    #take in user signin data
    #route it to db (POST)
    # query for db
    # return the username for header

    try:
        session['is_logged_in'] #validate if registration/login is successful, and send them to the wall if need be
        return redirect('/wall')
    except: pass
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    #handles the new user creation functions
    form = request.form #local copy to expedite processing
    print "I am form:",form
    #error handling:
    errors = False #sets up a state where "there are no errors" and we can call true when one is detected.

    # First Name - letters only, at least 2 characters and that it was submitted
    if not request.form[first_name]:
        errors = True
        flash('error', 'errors')
        first_name = request.form['first_name']

    # Last Name - letters only, at least 2 characters and that it was submitted
    last_name = request.form['last_name']

    # Email - Valid Email format, and that it was submitted
    email = request.form['email']

    # Password - at least 8 characters, and that it was submitted
    password = md5.new(request.form['password']).hexdigest();

    # Password Confirmation - matches password
    if form[confirm_password] != form[password]:
        errors = True
        flash('passwords do not match!', 'errors')

    insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    query_data = { 'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password }
    mysql.query_db(insert_query, query_data)
    return render_template('registration.html')

@app.route('/login')
def login():
    # logging in a user
    return render_template('wall.html')

@app.route('/logout', methods=['POST'])
def logOut():
    #logs us out, returns us to registration page.
    print "we are redirecting to '/'!"
    return redirect('/')

@app.route('/wall', methods=['POST']) #needs 'POST' method???
def wall(): #takes an ID???
    #displays the main comments page with comments and messages.

    #for displaying the comments page only?
    #has ability to reroute when new comments/messages update?
    return render_template('wall.html')

@app.route('/message')
def message():
    #for committing messages
    return render_template('wall.html')

@app.route('/comment')
def comment():
    #for committing comments
    return render_template('wall.html')

app.run(debug=True)


# INSERT INTO `wall_database`.`users` (`first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`) VALUES ('Paul', 'MacLachlan', 'me@mine.com', 'SECRET', 'NOW()', 'NOW()');
