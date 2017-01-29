from flask import Flask, render_template, session, flash, redirect, request
import random # for random int
import datetime # for timestamps

app = Flask(__name__)
app.secret_key = 'secretkeysarethebest' #resets session if you change this!


@app.route('/')
def ninjaGold():
    if not 'current_gold' in session: # default local host:5000 route
        session['current_gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
        # print type(session['activities'])
    return render_template('index.html')

@app.route('/process_money', methods=['POST']) #the labor of processing money
def process():
    # print request.form

    if request.form['building'] == 'farm':
        gold = random.randint(10,20)
        session['current_gold'] = session['current_gold'] + gold
        activity_text = "You earned",gold,"from the Farm!",datetime.datetime.now() # repeated, as text, trying to output the whole line into a preformattes string, not working need to revisit.
        print datetime.datetime.now()
        session['activities'].append(activity_text)
        # print type(session['activities'])
        # print session['activities']
        return redirect('/')

    elif request.form['building'] == 'cave':
        gold = random.randint(5,10)
        session['current_gold'] = session['current_gold'] + gold
        activity_text = "You earned",gold,"from the Cave!",datetime.datetime.now()
        print datetime.datetime.now()
        session['activities'].append(activity_text)
        return redirect('/')

    elif request.form['building'] == 'house':
        gold = random.randint(2,5)
        session['current_gold'] = session['current_gold'] + gold
        activity_text = "You earned",gold,"from the House!",datetime.datetime.now()
        print datetime.datetime.now()
        session['activities'].append(activity_text)
        return redirect('/')

    elif request.form['building'] == 'casino': # require more here from error output, dealing wiht negative vals as well as positive values
        gold = random.randint(-50,50)
        session['current_gold'] = session['current_gold'] + gold
        activity_text = "You earned",gold,"from the Cave!",datetime.datetime.now()
        print datetime.datetime.now()
        session['activities'].append(activity_text)
        return redirect('/')


@app.route('/secret_reset', methods = ['POST']) #again, reset functionality for cookies/session is here. Possibly not throurough as the redirect may not
def secretReset():
    session.clear()
    return redirect('/')


app.run(debug=True)
# source venv/bin/activate
