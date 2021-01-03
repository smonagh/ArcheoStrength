from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from starting_strength import create_app, db
from starting_strength.models import Workout
from flask_migrate import Migrate
from datetime import date

app = create_app()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/modify', methods=['POST', 'GET'])
def modify_data():

    if request.method == 'GET':
        return render_template("modify.html")

    elif request.method == 'POST':
        exercise = request.form.get("exercise")
        weight = float(request.form.get("weight"))
        rep_one = int(request.form.get("set_one"))
        rep_two = int(request.form.get("set_two"))
        rep_three = int(request.form.get("set_three"))
        exercise_date = process_input_date(request.form.get("exercise_date"))

        try:
            workout = Workout(exercise=exercise, weight=weight, rep_1=rep_one, rep_2=rep_two,
                            rep_3=rep_three, exercise_date=exercise_date)
            db.session.add(workout)
            db.session.commit()
        except Exception:
            return "Bad data input. Data point already exists. <a href='/'>Home </a>"

        return redirect(url_for('modify_data'))

    return render_template('modify.html')

@app.route('/view', methods=['GET'])
def view_data():
    return render_template("view.html")

@app.route('/today', methods=['GET'])
def todays_workout():
    return render_template("today.html")

def process_input_date(input_date):
    split_date = input_date.split('-')
    output_date = date(int(split_date[0]), int(split_date[1]), int(split_date[2]))

    return output_date