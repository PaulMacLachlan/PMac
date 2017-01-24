from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = 'secretsecret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    return render_template('results.html')

@app.route('/dojos')
def dojos():
    print 'I MADE IT TO DOJOS FAM'

app.run(debug=True)


# https://vimeo.com/200739328/bd298321b0
