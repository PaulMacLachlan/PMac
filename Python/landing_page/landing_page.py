from flask import Flask, render_template, request, flash # sets our methods to import
app = Flask(__name__)

@app.route('/') #our index page route
def landingPage():
    return render_template('index.html')

@app.route('/ninjas.html')
def ninjas():
    return render_template('/ninjas.html')

@app.route('/dojos.html')
def dojosNew():
    return render_template('dojos.html')

app.run(debug=True)
