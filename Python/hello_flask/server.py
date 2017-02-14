from flask import Flask, session, redirect, render_template, flash

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)

