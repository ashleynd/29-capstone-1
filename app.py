from flask import Flask, render_template, redirect, session, flash, g, abort, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Post
from forms import RegisterForm, LoginForm, AddPostForm, EditPostForm
import requests
from werkzeug.wrappers import AuthorizationMixin
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
        return render_template("/users/register.html", form=form)


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


@app.route("/feed")
def feed():
    """Show recent list of posts, most-recent first."""

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



@app.route("/favorites")
def favorites():
    """Favorites page for logged-in users only."""

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        return render_template("/posts/favorites.html")

@app.route("/buy")
def purchase_post():
    """Post with link to purchase."""

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        return render_template("/posts/purchase_post.html")


@app.route("/logout")
def logout():
    """Logs user out and redirects to homepage."""

    session.pop("user_id")

    return redirect("/")


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
        return render_template("/posts/my_posts.html", posts=posts, user_id=user_id)
    

@app.route('/posts/<int:post_id>', methods=["GET"])
def posts_show(post_id):
    """Show a post."""

    post = Post.query.get(post_id)
    return render_template('posts/purchase_post.html', post=post)




# @app.route('/posts/<int:post_id>/edit', methods=["POST"])
# def posts_update(post_id):
#     """Handle form submission for updating an existing post"""

#     post = Post.query.get_or_404(post_id)
#     post.title = request.form['title']
#     post.content = request.form['content']

#     db.session.add(post)
#     db.session.commit()
#     flash(f"Post '{post.title}' edited.")

#     return redirect(f"/users/{post.user_id}")


@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def posts_destroy(post_id):
    """Handle form submission for deleting an existing post"""

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()
    flash(f"Post '{post.title} deleted.")

    return redirect(f"/users/{post.user_id}")



#############################################################################
# 404 Page

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404