from flask import Flask, render_template, request, flash
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def resultPage():
    return render_template('result.html')

app.run(debug=True)
