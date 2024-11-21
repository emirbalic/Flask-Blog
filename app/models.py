from app import db  # Import db from app.py
from datetime import datetime

# Blog Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    title = db.Column(db.String(100), nullable=False)  # Title (max 100 characters)
    content = db.Column(db.Text, nullable=False)  # Post content
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)  # Default to current time

    def __repr__(self):
        return f"<Post {self.title}>"
