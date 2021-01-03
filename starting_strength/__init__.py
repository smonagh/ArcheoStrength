from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.static_folder = 'static'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///archeo_strength.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from starting_strength.models import db
    db.init_app(app)

    Migrate(app, db)

    return app
