from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

GENERIC_IMAGE_URL = "https://bethshalomsynagogue.org/wp-content/uploads/sites/77/2019/07/cancelled-stamp-4-e1562879608638.png"

db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    posts = db.relationship('Post', backref='user', cascade='all, delete-orphan')
    likes = db.relationship('Post', secondary="likes")


    def __repr__(self):
        return f"<User #{self.id}: {self.username}>"

    # start_register
    @classmethod
    def register(cls, username, password, first_name, last_name):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(password)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(first_name=first_name, last_name=last_name, username=username, password=hashed_utf8)

    
    # end_register

    # start_authenticate
    @classmethod
    def authenticate(cls, username, password):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, password):
            # return user instance
            return u
        else:
            return False
    # end_authenticate

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"


class Post(db.Model):
    """Posts model."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    # photo_url = db.Column(db.Text, nullable=False)
    purchase_url = db.Column(db.Text)
    caption = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")
    

    def photo_url(self):
        """Return image for post -- bespoke or generic."""
        
        return self.photo_url or GENERIC_IMAGE_URL

    def __repr__(self):
        return f"<Post Info: {self.id} {self.title} {self.purchase_url} {self.caption} {self.user_id}>"


class Likes(db.Model):
    """Mapping user likes to posts."""

    __tablename__ = 'likes' 

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='cascade'), unique=True)
