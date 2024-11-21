import os

# class Config:
#     # Base configuration
#     # SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
#     # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///instance/blog.db')
#     # SQLALCHEMY_TRACK_MODIFICATIONS = False
class Config:
    # Base configuration
    SECRET_KEY = 'your_secret_key'  # Replace with a strong secret key or use Flask's default for now
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/blog.db'  # Use relative path to SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for SQLAlchemy
    # Adjusting to absolute path to make sure it's correctly resolved
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'blog.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'instance', 'blog.db')
