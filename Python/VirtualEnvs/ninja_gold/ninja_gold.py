from flask import Flask, render_template, session

app = Flask(__name__)

@app.route('/')
def hello_name():
    return render_template('index.html', name="Paul", phrase="Hello", times=5) # localhost:5000/some_route

app.run(debug=True)
