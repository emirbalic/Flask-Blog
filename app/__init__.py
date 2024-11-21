from flask import Flask
from .models import db
from .routes import home, create_post, about  # Import route functions

def create_app():
    # Create Flask app
    app = Flask(__name__)

    # App config for the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/blog.db'  # Database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
    app.secret_key = 'secret'  # Secret key for session management

    # Initialize the database with the app
    db.init_app(app)

    # Register routes with app
    app.add_url_rule('/', 'home', home)  # Home page route
    app.add_url_rule('/create', 'create_post', create_post, methods=['GET', 'POST'])  # Create post route
    app.add_url_rule('/about', 'about', about)  # About page route

    return app
