from flask import Flask, request, render_template # Imports flask to allow us to create our application
app = Flask(__name__)      # Global var __name__ tells Flask whether or not we are running the file

@app.route('/') # the "@" symbol designaties a "Decorator" whicha rtached the following function to the '/'             #route. This means whatever we send a request to localhost:5000/ we will run the following          "hello_world" function.
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/hooray')
def hooray():
    return render_template('hooray.html')

app.run(debug=True)
