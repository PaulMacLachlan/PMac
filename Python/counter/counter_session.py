from flask import Flask, render_template, request, flash, session, redirect #all imports

app = Flask(__name__) #defines the flask app?

app.secret_key = 'ThisIsSecret' # necesary for session

@app.route('/') #tries to + session by 1, unless its already 1, then renders index.html.
def index():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/reset', methods=['POST']) #resets counter, prints in logs, sends us back to index.html again after reset.
def reset():
    session['counter'] = 0
    print session
    return redirect('/')

@app.route('/plusTwo', methods=['POST'])
def plusTwo():
    print "Im +2!"
    session['counter'] += 1
    print session['counter']
    return redirect('/')

app.run(debug=True)
