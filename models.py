from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

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

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)

    username = db.Column(db.Text, 
                         nullable=False, 
                         unique=True)

    password = db.Column(db.Text, 
                         nullable=False)

    posts = db.relationship('Post', backref='user', cascade='all, delete')

    # start_register
    @classmethod
    def register(cls, username, pwd):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8)
    # end_register

    # start_authenticate
    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False
    # end_authenticate    

class Post(db.Model):
    """Posts model."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    # photo_url = db.Column(db.Text)
    purchase_url = db.Column(db.Text)
    caption = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    
    # user = db.relationship('Post', backref='users', cascade="all, delete-orphan")



    # u = Post.query.filter_by(title=title).first()

    def photo_url(self):
        """Return image for post -- bespoke or generic."""
        
        return self.photo_url or GENERIC_IMAGE_URL

    def __repr__(self):
        return f"<Post Info: {self.id} {self.title} {self.purchase_url} {self.caption} {self.user_id}>"

