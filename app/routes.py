from flask import render_template, redirect, url_for, request, flash
from .models import db, Post

def initialize_routes(app):
    @app.route('/')
    @app.route('/home')
    def home():
        posts = Post.query.all()
        return render_template('home.html', posts=posts)

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/create_post', methods=['GET', 'POST'])
    def create_post():
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            if not title or not content:
                flash('Title and content are required!', 'danger')
                return redirect(url_for('create_post'))
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            flash('Post created successfully!', 'success')
            return redirect(url_for('home'))
        return render_template('create_post.html')
