from flask import Flask, render_template, request, flash
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def resultPage():
    print 'I\'m in the result page function'
    print request.form
    return render_template('result.html', data = request.form)

app.run(debug=True)
