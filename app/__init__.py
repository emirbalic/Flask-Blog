from flask import Flask
from .models import db
from .routes import main

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')

    # Configuration settings (e.g., secret key, database URI)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # Register Blueprints (routes)
    app.register_blueprint(main)

    return app
