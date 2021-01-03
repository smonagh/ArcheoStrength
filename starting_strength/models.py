from starting_strength import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(30), nullable=False)
    weight = db.Column(db.Float(), nullable=False)
    exercise_date = db.Column(db.Date())
    rep_1 = db.Column(db.Integer(), nullable=False)
    rep_2 = db.Column(db.Integer(), nullable=False)
    rep_3 = db.Column(db.Integer(), nullable=False)

    __table_args__ = (db.UniqueConstraint('exercise', 'exercise_date'),)

    def __init__(self, exercise, weight, exercise_date, rep_1, rep_2, rep_3):
        self.exercise = exercise
        self.weight = weight
        self.exercise_date = exercise_date
        self.rep_1 = rep_1
        self.rep_2 = rep_2
        self.rep_3 = rep_3


    def __repr__(self):
        return '<Exercise {0} : Date {1} >'.format(self.exercise, self.exercise_date)