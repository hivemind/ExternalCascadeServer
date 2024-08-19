from flask import Flask

from app.extensions import db


def app_factory():

    app = Flask(__name__)

    # Configure the SQLAlchemy part of the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///options.db'  # Use SQLite for simplicity
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app

