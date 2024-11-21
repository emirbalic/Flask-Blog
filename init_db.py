from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)

    # Import and register routes
    with app.app_context():
        from .routes import initialize_routes
        initialize_routes(app)

        # Create the database tables if they don't exist
        db.create_all()

    return app
