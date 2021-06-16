from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length, URL, Optional


class RegisterForm(FlaskForm):
    """Form for registering a user."""

    first_name = TextAreaField("First Name", validators=[InputRequired()])
    last_name = TextAreaField("Last Name", validators=[InputRequired()])
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class LoginForm(FlaskForm):
    """Form for registering a user."""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class AddPostForm(FlaskForm):
    """Form for adding posts."""

    title = StringField("Title", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[URL()])
    purchase_url = StringField("Link to where to purchase item", validators=[URL()])
    caption = TextAreaField("Photo caption", validators=[Optional()])

class EditPostForm(FlaskForm):
    """Form for editing posts."""

    title = StringField("Title", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    purchase_url = StringField("Link to where to purchase item", validators=[URL()])
    caption = TextAreaField("Photo caption", validators=[Optional()])

class DeleteForm(FlaskForm):
    """Delete form."""

