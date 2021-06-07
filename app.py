

from flask import Flask, render_template, redirect, session, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Post
from forms import RegisterForm, LoginForm, AddPostForm, EditPostForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///picslink"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SECRET_KEY"] = "abc123"

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user: produce form & handle form submission."""

    form = RegisterForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data

        user = User.register(name, pwd)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id

        # on successful login, redirect to user feed page
        return redirect("/feed")

    else:
        return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Produce login form or handle login."""

    form = LoginForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data

        # authenticate will return a user or False
        user = User.authenticate(name, pwd)

        if user:
            session["user_id"] = user.id  # keep logged in
            return redirect("/feed")

        else:
            form.username.errors = ["Bad name/password"]

    return render_template("login.html", form=form)
# end-login    


@app.route("/feed")
def feed():
    """Feed page for logged-in users only."""

    # posts = Post.query.all()

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

        # alternatively, can return HTTP Unauthorized status:
        #
        # from werkzeug.exceptions import Unauthorized
        # raise Unauthorized()

    else:
        return render_template("feed.html")

@app.route("/favorites")
def favorites():
    """Favorites page for logged-in users only."""

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        return render_template("favorites.html")

@app.route("/myposts")
def myposts():
    """Posts page for logged-in users only."""

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        return render_template("myposts.html")


@app.route("/logout")
def logout():
    """Logs user out and redirects to homepage."""

    session.pop("user_id")

    return redirect("/")

# @app.route('/newpost')
# def post_add():
#     """Add a post."""

#     return render_template('newpost.html')

@app.route('/add', methods=["GET", "POST"])
def add_post():
    """Add a post."""

    form = AddPostForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_post = Post(**data)
        # new_post = Post(title=form.title.data, photo_url=form.photo_url.data, caption=form.caption.data)
        db.session.add(new_post)
        db.session.commit()
        flash(f"{new_post.title} added.")
        return redirect(url_for('list_posts'))

    else:
        # re-present form for editing
        return render_template("newpost.html", form=form)

@app.route("/")
def list_posts():
    """List all posts."""

    posts = Post.query.all()
    return render_template("post_list.html", posts=posts)

@app.route("/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    """Edit post."""

    post = Post.query.get_or_404(post_id)
    form = EditPostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.photo_url = form.photo_url.data
        post.caption = form.caption.data
        db.session.commit()
        flash(f"{post.title} updated.")
        return redirect('/feed')

    else:
        # failed; re-present form for editing
        return render_template("edit_newpost.html", form=form, post=post)
