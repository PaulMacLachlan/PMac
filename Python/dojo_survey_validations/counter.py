from flask import Flask, render_template, request, flash, session, redirect
app = Flask(__name__)

app.secret_key = "SECRET"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def resultPage():
    error_messages = {} #ideally, there is a way to eval ALL possible error situations, store their given error messages, and server each of those error(s) to the page where appropriate. Here, we are hitting the first error we encounter, and not considering ALL CASES when outputting errors.
    print request.form
    if len(request.form['name']) <= 0:
        error_messages['name_error'] = "* Name is required"
        flash(error_messages['name_error'])#individual error messages for Name and Comments not being present.
        return redirect ('/')

    if len(request.form['comment']) <= 0:
        error_messages['comment_required'] = "* Comments are required"
        flash(error_messages['comment_required'])#individual error messages for Name and Comments not being present.
        return redirect ('/')

    if len(request.form['comment']) > 120:
        error_messages['comment_long'] = "* Comments can be no more that 120 characters"
        flash(error_messages['comment_long'])#individual error messages for Name and Comments not being present.
        return redirect ('/')
    else:
        return render_template('result.html', data = request.form)

    for keys in error_messages:
        errors_list = []
        errors_list.append(keys)
        print errors_list
app.run(debug=True)
