from flask import render_template, url_for, flash, redirect
from blog_package import app, db, bcrypt
from blog_package.forms import RegistrationForm, LoginForm
from blog_package.models import User, Post
from flask_login import login_user, current_user, logout_user

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
    return render_template("index.html", posts=posts, token="flask react", is_logged_in=current_user.is_authenticated)

@app.route('/about')
def renderAbout():
    return render_template("about.html", is_logged_in=current_user.is_authenticated)

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
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def renderLogin():
    if current_user.is_authenticated:
        return redirect(url_for("renderHomePage"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("renderHomePage"))
        else:
            flash("Login unsuccessful. Please check email and/or password.", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def renderLogout():
    logout_user()
    return redirect(url_for("renderHomePage"))

