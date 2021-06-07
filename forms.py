from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length, URL, Optional


class RegisterForm(FlaskForm):
    """Form for registering a user."""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class LoginForm(FlaskForm):
    """Form for registering a user."""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])



class AddPostForm(FlaskForm):
    """Form for adding posts."""

    title = StringField("Title", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    caption = TextAreaField("Photo caption", validators=[Optional(), Length(min=10)])

class EditPostForm(FlaskForm):
    """Form for editing posts."""

    title = StringField("Title", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    caption = TextAreaField("Photo caption", validators=[Optional(), Length(min=10)])