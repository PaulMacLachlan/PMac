from flask import Flask, render_template, session, flash, redirect, request
import random
import datetime

app = Flask(__name__)
app.secret_key = 'secretkeysarethebest' #resets session!!!


@app.route('/')
def ninjaGold():
    if not 'current_gold' in session:
        session['current_gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
        # print type(session['activities'])
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    # print request.form

    if request.form['building'] == 'farm':
        gold = random.randint(10,20)
        session['current_gold'] = session['current_gold'] + gold
        activity_text = "You earned",gold,"from the Farm!",datetime.datetime.now()
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

    elif request.form['building'] == 'casino':
        gold = random.randint(-50,50)
        session['current_gold'] = session['current_gold'] + gold
        activity_text = "You earned",gold,"from the Cave!",datetime.datetime.now()
        print datetime.datetime.now()
        session['activities'].append(activity_text)
        return redirect('/')


@app.route('/secret_reset', methods = ['POST'])
def secretReset():
    session.clear()
    return redirect('/')


app.run(debug=True)
# source venv/bin/activate
