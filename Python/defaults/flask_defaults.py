import flask from Flask, render_template, redirect, session, flash
import random

# secret is for session.
app.secret_key = 'ThisIsSecretDontTellAnyone'

@app.route('/')
def routeA():
    print 'Im in route A'

@app.route('/routeB')
def routeB():
    print 'Im in route B'


app.run(debug=True)
