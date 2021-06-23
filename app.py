from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Post
from forms import RegisterForm, LoginForm, AddPostForm, DeleteForm, EditPostForm
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', "postgres:///picslink").replace("://", "ql://", 1)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY', 'hellosecret1')
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


#############################################################################
# Registration Route

@app.route("/register", methods=["GET", "POST"])
def register():
    """Registers a new user."""

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
        flash('Welcome! Successfully Created Your Account. ✅', "success")
        return redirect("/feed")

    return render_template('/users/register.html', form=form)


#############################################################################
# Login/Logout Routes

@app.route("/login", methods=["GET", "POST"])
def login():
    """Login form to handle login."""

    form = LoginForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data

        # authenticate will return a user or False
        user = User.authenticate(name, pwd)

        if user:
            session["user_id"] = user.id  # keep logged in
            flash(f"Welcome back, {user.first_name}! 👋🏻", "success")
            return redirect("/feed")

        else:
            form.username.errors = ["Incorrect name/password"]

    return render_template("/users/login.html", form=form)
# end-login    

@app.route("/logout")
def logout():
    """Logs user out and redirects to homepage."""

    session.pop("user_id")
    flash("You have successfully logged out. See you later! 👋🏻")
    return redirect("/")

#############################################################################
# Feed Routes

@app.route("/")
def homepage():
    """Shows a public list of posts for not logged-in users, most-recent first."""

    posts = Post.query.order_by(Post.created_at.desc())
    return render_template("index.html", posts=posts)

@app.route("/feed")
def feed():
    """Shows list of posts for logged-in users, most-recent first."""

    posts = Post.query.order_by(Post.created_at.desc())

    if "user_id" not in session:
        flash("🚫 You must be logged in to view your feed.")
        return redirect("/")

    else:
        # print('**********************')
        # print(posts[1].photo_url)
        # print('**********************')
        form = DeleteForm()
        return render_template("/posts/feed.html", posts=posts, form=form)


#############################################################################
# Post Routes

@app.route('/add', methods=["GET", "POST"])
def add_post():
    """Adds a post."""

    if "user_id" not in session:
        flash("🚫 You must be logged in to create posts.")
        return redirect("/")

    form = AddPostForm()

    if form.validate_on_submit():
        # data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        # new_post = Post(**data)
        # image = form.image.data
        title = form.title.data
        photo_url = form.photo_url.data
        purchase_url = form.purchase_url.data
        caption = form.caption.data
        user_id = session["user_id"]


        new_post = Post(user_id=user_id, title=title, photo_url=photo_url, purchase_url=purchase_url, caption=caption)
        db.session.add(new_post)
        db.session.commit()
        flash(f"New post: {new_post.title} added. 👏🏻")
        return redirect("/myposts")

    else:
        # re-present form for editing
        return render_template('/posts/add_post_form.html', form=form)


@app.route("/myposts")
def my_posts():
    """Page to show just the posts the user created."""

    if "user_id" not in session:
        flash("🚫 You must be logged in to create posts.")
        return redirect("/")

    else:
        user_id = session["user_id"]
        posts = Post.query.filter(user_id==Post.user_id)
        form = DeleteForm()
        return render_template("/posts/my_posts.html", posts=posts, user_id=user_id, form=form)


@app.route("/posts/<int:post_id>/update", methods=["GET", "POST"])
def update_post(post_id):
    """Edit form for user's posts."""

    post = Post.query.get(post_id)

    if "user_id" not in session:
        flash("🚫 You must be logged in to edit posts.")
        return redirect("/")

    form = EditPostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.photo_url = form.photo_url.data
        post.purchase_url = form.purchase_url.data
        post.caption = form.caption.data

        db.session.commit()
        flash(f"New post: {post.title} updated. 👍🏻")
        return redirect("/myposts")

    return render_template("posts/post_edit.html", form=form, post=post)

#############################################################################
# Delete Route

@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    """Deletes a post the user created."""

    post = Post.query.get(post_id)
    if "user_id" not in session:
        flash("🚫 You must be logged in to delete posts.")
        return redirect("/")

    form = DeleteForm()

    if form.validate_on_submit():
        db.session.delete(post)
        db.session.commit()

    flash(f"Post successfully deleted. ☑️")
    return redirect("/myposts")
    

#############################################################################
# Favorite Routes

# @app.route("/posts/<int:post_id>/favorite", methods=["POST"])
# def add_favorite(post_id):
#     """Favorite post."""

#     if "user_id" not in session:
#         flash("🚫 You must be logged in to favorite posts.")
#         return redirect("/")

#     favorite = Favorite(user_id = session["user_id"], post_id=post_id)
#     db.session.add(favorite)
#     db.session.commit()
#     return redirect("/favorites")

# @app.route("/favorites")
# def show_favorites():
#     """Page to show all the posts the user favorited."""

#     if "user_id" not in session:
#         flash("🚫 You must be logged in to add favorites.")
#         return redirect("/")

#     else:
#         user_id = session["user_id"]
#         user = User.query.get_or_404(user_id)
#         return render_template("/posts/favorites.html", user=user)


#############################################################################
# 404 Page

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404