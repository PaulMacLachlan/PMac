from flask import Flask, session, render_template, redirect, flash

app = Flask(__name__)

app.secret_key = "keepitsecretkeepitsafe"

#render values as actual filenames? "donatello.jpg" etc?
ninja_color = {
    'purple': "Donatello",
    'blue': "Leonardo",
    'orange': "Michaelangelo",
    'red': "Raphael"
}
#var for null = April

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/ninja')
def allNinjas():
    return render_template('/ninja.html')

@app.route('/ninja/<color>')
def ninjaColor(color):
    #ninja = none
    try:
        ninja = ninja_color[color]
    except:
        ninja = "notapril"
    ninja += '.jpg'
    return render_template("ninja_color.html", color=ninja_color, none=april)

app.run(debug=True)
