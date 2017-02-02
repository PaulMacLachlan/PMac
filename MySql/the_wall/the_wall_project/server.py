from flask import Flask, session, render_template, redirect, flash

app = Flask(__name__)
app.secret_key = "SUPERSECRET"

from mysqlconnection import MySQLConnector
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'wall_database')
# an example of running a query
print mysql.query_db("SELECT * FROM users")

@app.route('/', methods=['POST', 'GET'])
def index():
    #error if no input provided
    #take in user signin data
    #route it to db (POST)
    # query for db
    # return the username for header
    return render_template('registration.html')

@app.route('/logout', methods=['POST'])
def logOut():
    print "we are redirecting to '/'!"
    return redirect('/')

@app.route('/wall', methods=['POST']) #needs 'POST' method???
def wall(): #takes an ID???
    #for displaying the comments page only?
    #has ability to reroute when new comments/messages update?
    return render_template('wall.html')

app.run(debug=True)


# INSERT INTO `wall_database`.`users` (`first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`) VALUES ('Paul', 'MacLachlan', 'me@mine.com', 'SECRET', 'NOW()', 'NOW()');
