from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = 'secretsecret'

@app.route('/')
def home():
        try:
            session['counter'] += 1
        except:
            session['counter'] = 1
        return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    username = request.form['Username']
    password = request.form['Password']
    return render_template('results.html', username = username)

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

app.run(debug=True)





# https://vimeo.com/200739328/bd298321b0
