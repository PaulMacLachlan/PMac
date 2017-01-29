from flask import Flask, render_template, request, flash, session, redirect
app = Flask(__name__)

app.secret_key = "SECRET"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def resultPage():
    print 'I\'m in the result page function'
    print request.form
    if len(request.form['name']) <= 0:
        flash("* Name is required")#individual error messages for Name and Comments not being present.
        print flash # trying to see flash messages to see if multiple could be printed or if only one message at a time is supported.
        return redirect ('/')

    elif len(request.form['comment']) <= 0:
        flash("* Comments are required")#individual error messages for Name and Comments not being present.
        print flash # trying to see flash messages to see if multiple could be printed or if only one message at a time is supported.
        return redirect ('/')
    else:
        return render_template('result.html', data = request.form)

app.run(debug=True)
