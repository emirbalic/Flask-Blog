from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret'

db = SQLAlchemy(app)

# Blog Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    title = db.Column(db.String(100), nullable=False)  # Title (max 100 characters)
    content = db.Column(db.Text, nullable=False)  # Post content
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)  # Default to current time

    def __repr__(self):
        return f"<Post {self.title}>"
@app.route('/')
def home():
    posts = Post.query.all()  # Fetch all posts from the database
    return render_template('home.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Form validation: ensure both fields are filled
        if not title or not content:
            flash("Both title and content are required!")
            return redirect(url_for('create_post'))

        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create_post.html')
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)