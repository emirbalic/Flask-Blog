from flask import render_template, redirect, url_for, flash
from flask import Blueprint
from .forms import PostForm
from .models import db, Post

main = Blueprint('main', __name__)

@main.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@main.route('/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_post = Post(title=title, content=content)

        db.session.add(new_post)
        db.session.commit()

        flash('Post created successfully!', 'success')
        return redirect(url_for('main.home'))

    return render_template('create_post.html', form=form)
