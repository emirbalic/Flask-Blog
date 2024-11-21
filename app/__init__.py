from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # Initialize the database
    db.init_app(app)

    # Register routes
    from .routes import register_routes
    register_routes(app)

    return app
