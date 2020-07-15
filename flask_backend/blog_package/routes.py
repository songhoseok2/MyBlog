import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from blog_package import app, db, bcrypt
from blog_package.forms import RegistrationForm, LoginForm, UpdateAccountForm
from blog_package.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        "author": "John",
        "title": "Blog Post 1",
        "content": "First pots content",
        "date_posted": "April 20, 2018"
    },
    {
        "author": "Dave",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "June 21, 2013"
    },
    {
        "author": "John",
        "title": "Blog Post 1",
        "content": "First pots content",
        "date_posted": "April 20, 2018"
    },
    {
        "author": "Dave",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "June 21, 2013"
    },
    {
        "author": "John",
        "title": "Blog Post 1",
        "content": "First pots content",
        "date_posted": "April 20, 2018"
    },
    {
        "author": "Dave",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "June 21, 2013"
    }
]


@app.route('/')
def renderHomePage():
    return render_template("index.html", posts=posts, token="flask react", is_logged_in=str(current_user.is_authenticated))

@app.route('/about')
def renderAbout():
    return render_template("about.html", is_logged_in=str(current_user.is_authenticated))

@app.route("/register", methods=["GET", "POST"])
def renderRegister():
    if current_user.is_authenticated:
        return redirect(url_for("renderHomePage"))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("renderLogin"))
    return render_template("register.html", title="Register", form=form, is_logged_in=str(current_user.is_authenticated))

@app.route("/login", methods=["GET", "POST"])
def renderLogin():
    if current_user.is_authenticated:
        return redirect(url_for("renderHomePage"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("renderHomePage"))
        else:
            flash("Login unsuccessful. Please check email and/or password.", "danger")
    return render_template("login.html", title="Login", form=form, is_logged_in=str(current_user.is_authenticated))

@app.route("/logout")
def renderLogout():
    logout_user()
    return redirect(url_for("renderHomePage"))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_fn)
    form_picture.save(picture_path)
    return picture_fn

@app.route("/account",  methods=["GET", "POST"])
@login_required
def renderAccount():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated.", "success")
        return redirect(url_for("renderAccount"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("account.html", title="Account", is_logged_in=str(current_user.is_authenticated), image_file=image_file, form=form)

