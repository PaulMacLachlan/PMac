from flask import Flask, render_template, request, flash # sets our methods to import
app = Flask(__name__)

@app.route('/') #our index page route
def landingPage():
    return render_template('index.html', style = ../static/style.css)

@app.route('/ninjas.html')
def ninjas():
    return render_template('/ninjas.html', style = ../static/style.css)

@app.route('/dojos.html')
def dojosNew():
    return render_template('dojos.html', style = ../static/style.css)

app.run(debug=True)
