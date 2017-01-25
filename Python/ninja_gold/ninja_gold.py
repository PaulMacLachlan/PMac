from flask import Flask, render_template, session, flash, redirect
import random

app = Flask(__name__)

@app.route('/')
def ninjaGold():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def processFarm(): #heres where the problem is, need the maths!
    if session['farm'] != 0:
        print "You chose Farm!"
        procFarm = random.randint(10,20)
        print procFarm
        return redirect('/', gold = 'current_gold')

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
