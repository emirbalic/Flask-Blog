from flask import render_template, request, redirect, url_for, flash
from . import db  # Import db from app.py
from .models import Post  # Import Post model directly
from .forms import PostForm

# Home route
def home():
    posts = Post.query.all()  # Fetch all posts from the database
    return render_template('home.html', posts=posts)

# Create post route with the form
def create_post():
    form = PostForm()

    if form.validate_on_submit():  # Check if the form is submitted and valid
        title = form.title.data
        content = form.content.data

        # Create a new post object and add it to the database
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        flash('Post Created!', 'success')
        return redirect(url_for('home'))  # Redirect to the home page after creating a post

    return render_template('create_post_wtf.html', form=form)



# # Create post route
# def create_post():
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#
#         # Form validation
#         if not title or not content:
#             flash("Both title and content are required!")
#             return redirect(url_for('create_post'))
#
#         new_post = Post(title=title, content=content)
#         db.session.add(new_post)
#         db.session.commit()
#
#         return redirect(url_for('home'))  # Redirect to home after creating a post
#
#     return render_template('create_post.html')

# About route
def about():
    return render_template('about.html')

def post_detail(post_id):
    post = Post.query.get_or_404(post_id)  # Get the post by ID or return a 404 if not found
    return render_template('post_detail.html', post=post)


# Edit post route
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)  # Fetch the post by its ID
    form = PostForm(obj=post)  # Pre-populate the form with the existing post data

    if request.method == 'POST' and form.validate_on_submit():
        post.title = form.title.data  # Update the post title
        post.content = form.content.data  # Update the post content

        db.session.commit()  # Save the changes to the database

        flash('Post updated successfully!', 'success')
        return redirect(url_for('home'))  # Redirect back to the home page

    return render_template('edit_post.html', form=form, post=post)

# Register routes
def register_routes(app):
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/create', 'create_post', create_post, methods=['GET', 'POST'])
    app.add_url_rule('/about', 'about', about)
    app.add_url_rule('/post/<int:post_id>', 'post_detail', post_detail)  # Dynamic route for post detail
    app.add_url_rule('/edit/<int:post_id>', 'edit_post', edit_post, methods=['GET', 'POST'])  # New edit route

