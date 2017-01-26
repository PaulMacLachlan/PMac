from flask import Flask, render_template, session, request, flash, redirect
import random

app = Flask(__name__)
#this needs to be here to make session work
app.secret_key = 'YouWereMissingThis'

@app.route('/')
def ninjaGold():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def processFarm(): #heres where the problem is, need the maths!
#I changed your "name" values in your html, they should all be the same, and the "value" should be different, i.e. farm, cave, house, casino, the if statement for farm below represents how to call it. I'm still getting that key error and I don't know why.
    if request.form['building'] == 'farm':
        print "You chose Farm!"
        procFarm = random.randint(10,20)
        print procFarm
        session['current_gold'] += procFarm
        print session['current_gold']
        return redirect('/', session['gold'])

    elif session['cave'] != 0:
        print "You chose Cave!"
        procFarm = random.randint(5,10)
        print procFarm
        return redirect('/', gold = 'current_gold')

    elif session['house'] != 0:
        print "You chose House!"
        procFarm = random.randint(2,5)
        print procFarm
        return redirect('/', gold = 'current_gold')

    elif session['casino'] != 0:
        print "You chose Casino!"
        procFarm = random.randint(0,50)
        print procFarm
        return redirect('/', gold = 'current_gold')

app.run(debug=True)
# source venv/bin/activate
