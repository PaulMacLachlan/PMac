from flask import Flask, render_template, session, flash, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'secretkeysarethebest' #resets session!!!


@app.route('/')
def ninjaGold():
    if not 'current_gold' in session:
        session['current_gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    print request.form

    if request.form['building'] == 'farm':
        print "You chose Farm!"
        gold = random.randint(10,20)
        print "you won",gold,"gold!"
        session['current_gold'] = session['current_gold'] + gold
        print "we updated gold!"
        print "total gold is now",session['current_gold'],"!"
        return redirect('/')

    elif request.form['building'] == 'cave':
        print "You chose Cave!"
        gold = random.randint(5,10)
        print "you won",gold,"gold!"
        session['current_gold'] = session['current_gold'] + gold
        print "we updated gold!"
        print "total gold is now",session['current_gold'],"!"
        return redirect('/')

    elif request.form['building'] == 'house':
        print "You chose House!"
        gold = random.randint(2,5)
        print "you won",gold,"gold!"
        session['current_gold'] = session['current_gold'] + gold
        print "we updated gold!"
        print "total gold is now",session['current_gold'],"!"
        return redirect('/')

    elif request.form['building'] == 'casino':
        print "You chose Casino!"
        gold = random.randint(-50,50)
        print "you won",gold,"gold!"
        session['current_gold'] = session['current_gold'] + gold
        print "we updated gold!"
        print "total gold is now",session['current_gold'],"!"
        return redirect('/')

app.run(debug=True)
# source venv/bin/activate
