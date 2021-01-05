from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from starting_strength import create_app, db
from starting_strength.models import Workout
from flask_migrate import Migrate
from datetime import date
from starting_strength.generate_plot import generate_image

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

        if verify_in_database(exercise, exercise_date):
            try:
                workout = Workout.query.filter_by(exercise=exercise, exercise_date=exercise_date).first()
                workout.weight = weight
                workout.rep_1 = rep_one
                workout.rep_2 = rep_two
                workout.rep_3 = rep_three
                db.session.add(workout)
                db.session.commit()
                return redirect(url_for('modify_data'))
            except Exception:
                db.session.rollback()
                return "Ran into error. <a href='/'> Home </a>"

        try:
            workout = Workout(exercise=exercise, weight=weight, rep_1=rep_one, rep_2=rep_two,
                              rep_3=rep_three, exercise_date=exercise_date)
            db.session.add(workout)
            db.session.commit()
            return redirect(url_for('modify_data'))
        except Exception:
            db.session.rollback()
            return "Bad data input. Data point already exists. <a href='/'>Home </a>"

        return redirect(url_for('modify_data'))

    return render_template('modify.html')

@app.route('/view/<exercise>', methods=['GET'])
def view_data(exercise):
    data_dict = {'exercise': [], 'weight': [], 'rep_one': [], 'rep_two': [], 'rep_three': [], 'date': []}
    permissible_exercises = ['bench', 'overhead', 'squat', 'deadlift', 'pull-down', 'row', 'kickback']

    if not exercise:
        return render_template("view.html", exercise_data=data_dict)

    if exercise in permissible_exercises:
        data_dict = get_view_data(exercise, data_dict)
        generate_image(exercise, data_dict)
        return render_template("view.html", exercise_data=data_dict)

    else:
        return redirect(url_for('index'))

@app.route('/today', methods=['GET'])
def todays_workout():
    return render_template("today.html")

def process_input_date(input_date):
    split_date = input_date.split('-')
    output_date = date(int(split_date[0]), int(split_date[1]), int(split_date[2]))

    return output_date

@app.after_request
def add_header(r):
    
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

def get_view_data(exercise, data_dict):

    query_result = db.session.query(Workout).filter_by(exercise=exercise).order_by(Workout.exercise_date).all()

    for row in query_result:
        data_dict['exercise'].append(row.exercise)
        data_dict['weight'].append(row.weight)
        data_dict['rep_one'].append(row.rep_1)
        data_dict['rep_two'].append(row.rep_2)
        data_dict['rep_three'].append(row.rep_3)
        data_dict['date'].append(row.exercise_date)

    return data_dict

def verify_in_database(exercise, exercise_date):
    
    query_result = db.session.query(Workout).filter_by(exercise=exercise, exercise_date=exercise_date).first()

    if query_result:
        return True

    return False