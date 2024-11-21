
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# This will be initialized later
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)  # Create a new Flask app instance
    app.config.from_object(Config)  # Apply the config settings

    db.init_app(app)  # Initialize db with the app

    from routes import register_routes  # Import routes after db initialization
    register_routes(app)

    return app








# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from models import db, Post  # Import db and Post from models.py
# from config import Config  # Import the config class
#
# from routes import register_routes  # Import register_routes
#
# # Initialize db globally to be used in models
# db = SQLAlchemy()
#
# def create_app():
#     app = Flask(__name__)  # Create a new Flask app instance
#     app.config.from_object(Config)  # Apply the config settings
#
#     db.init_app(app)  # Initialize db with the app
#
#     # Register routes after the app is initialized
#     register_routes(app)
#
#     return app
#







# app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # SQLite database
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # app.secret_key = 'secret'
# app.config.from_object(Config)
#
#
# db.init_app(app)  # Initialize db with the app#
#
#
# @app.route('/')
# def home():
#     posts = Post.query.all()  # Fetch all posts from the database
#     return render_template('home.html', posts=posts)
#
# @app.route('/create', methods=['GET', 'POST'])
# def create_post():
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#
#         # Form validation: ensure both fields are filled
#         if not title or not content:
#             flash("Both title and content are required!")
#             return redirect(url_for('create_post'))
#
#         new_post = Post(title=title, content=content)
#         db.session.add(new_post)
#         db.session.commit()
#
#         return redirect(url_for('home'))
#
#     return render_template('create_post.html')
# @app.route('/about')
# def about():
#     return render_template('about.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)