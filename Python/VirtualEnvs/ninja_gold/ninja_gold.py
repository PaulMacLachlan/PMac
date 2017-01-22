from flask import Flask, render_template, session

app = Flask(__name__)

@app.route('/')
def ninjaGold():
    return render_template('index.html', name="ninja", phrase="farm") # localhost:5000/some_route

app.run(debug=True)
