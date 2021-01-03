from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/modify')
def modify_data():
    return render_template("modify.html")

@app.route('/view')
def view_data():
    return render_template("view.html")

@app.route('/today')
def todays_workout():
    return render_template("today.html")