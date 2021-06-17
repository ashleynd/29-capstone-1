from flask import Flask, render_template, redirect, session, flash, g, abort, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Post
from forms import RegisterForm, LoginForm, AddPostForm, EditPostForm, DeleteForm
import requests
from sqlalchemy.exc import IntegrityError
# from werkzeug.wrappers import AuthorizationMixin
# from imgurpython import ImgurClient
# from secrets import client_id, client_secret, access_token, refresh_token

CURR_USER_KEY = "curr_user"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///picslink"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SECRET_KEY"] = "abc123"


toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


# client = ImgurClient(client_id, client_secret, access_token, refresh_token)

# BASE_HTTP_ENDPOINT = https://api.imgur.com/3/

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


#############################################################################
# Registration Routes

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User.register(username, password, first_name, last_name)

        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append('Username taken.  Please pick another')
            return render_template('/users/register.html', form=form)
        session["user_id"] = user.id
        flash('Welcome! Successfully Created Your Account!', "success")
        return redirect("/feed")

    return render_template('/users/register.html', form=form)


#############################################################################
# Login/Logout Routes

@app.route("/login", methods=["GET", "POST"])
def login():
    """Produce login form or handle login."""

    # session[CURR_USER_KEY] = user.id

    form = LoginForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data

        # authenticate will return a user or False
        user = User.authenticate(name, pwd)

        if user:
            session["user_id"] = user.id  # keep logged in
            flash(f"Welcome back, {user.first_name}!", "success")
            return redirect("/feed")

        else:
            form.username.errors = ["Incorrect name/password"]

    return render_template("/users/login.html", form=form)

    #     do_login(user)
    #     flash(f”Hello, {user.username}!“, “success”)
    #     return redirect(f”/users/{user.id}“)
    # else:
    #     form.username.errors = [“Invalid username/password.“]
    #     flash(“Invalid credentials.“, ‘danger’)
    #     return render_template(“users/login_user_form.html”, form=form)
# end-login    

@app.route("/logout")
def logout():
    """Logs user out and redirects to homepage."""

    session.pop("user_id")

    return redirect("/")


#############################################################################
# Feed Route

@app.route("/")
def homepage():
    """Show homepage. A recent list of posts for not logged-in users, most-recent first."""

    posts = Post.query.order_by(Post.created_at.desc())

    return render_template("index.html", posts=posts)


@app.route("/feed")
def feed():
    """Show recent list of posts for logged-in users, most-recent first."""

    # """
    # Extracts the items (images) on the front page of Imgur.
    # For logged-in users only.
    # """
    # url = "https://api.imgur.com/3/gallery/top/time/week/2?showViral=false&mature=false&album_previews=false"
    # headers = {'Authorization': 'Client-ID 9b315a3d4a73278'}
    # response = requests.request("GET", url, headers=headers)
    # print(response)

    # posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    posts = Post.query.order_by(Post.created_at.desc())

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        return render_template("/posts/feed.html", posts=posts)

#############################################################################
# Favorites Route

@app.route("/favorites")
def favorites():
    """Favorites page for logged-in users only."""

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        return render_template("/posts/favorites.html")


#############################################################################
# Post Routes

@app.route('/add', methods=["GET", "POST"])
def add_post():
    """Add a post."""

    form = AddPostForm()

    if form.validate_on_submit():
        # data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        # new_post = Post(**data)
        title = form.title.data
        photo_url = form.photo_url.data
        purchase_url = form.purchase_url.data
        caption = form.caption.data
        user_id = session["user_id"]


        new_post = Post(user_id=user_id, title=title, photo_url=photo_url, purchase_url=purchase_url, caption=caption)
        db.session.add(new_post)
        db.session.commit()
        flash(f"Added new post: {new_post.title} added.")
        return redirect("/myposts")

    else:
        # re-present form for editing
        return render_template('/posts/add_post_form.html', form=form)


@app.route("/myposts")
def my_posts():
    """Posts page for logged-in users only."""

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        user_id = session["user_id"]
        posts = Post.query.filter(user_id==Post.user_id)
        form = DeleteForm()
        return render_template("/posts/my_posts.html", posts=posts, user_id=user_id, form=form)
    

@app.route('/posts/<int:post_id>', methods=["GET"])
def posts_show(post_id):
    """Show a post."""

    p = Post.query.get(post_id)
    return render_template('posts/purchase_post.html', post=p)


@app.route("/buy")
def purchase_post():
    """Post with link to purchase."""

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        return render_template("/posts/purchase_post.html")


@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    """Delete post."""

    post = Post.query.get(post_id)
    if "user_id" not in session:
        flash("You must be logged in to delete posts.")
        return redirect("/")

    form = DeleteForm()

    if form.validate_on_submit():
        db.session.delete(post)
        db.session.commit()

    return redirect("/myposts")

#############################################################################
# Like routes


@app.route('/users/<int:user_id>/likes', methods=["GET"])
def show_likes(user_id):
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = User.query.get_or_404(user_id)
    return render_template('users/likes.html', user=user, likes=user.likes)


@app.route('/posts/<int:post_id>/like', methods=['POST'])
def add_like(post_id):
    """Toggle a liked post for the currently-logged-in user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/feed")

    liked_post = Post.query.get_or_404(post_id)
    if liked_post.user_id == g.user.id:
        return abort(403)

    user_likes = g.user.likes

    if liked_post in user_likes:
        g.user.likes = [like for like in user_likes if like != liked_post]
    else:
        g.user.likes.append(liked_post)

    db.session.commit()

    return redirect("/feed")



#############################################################################
# 404 Page

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404