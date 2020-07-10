from flask import render_template, url_for, flash, redirect
from blog_package import app, db, bcrypt
from blog_package.forms import RegistrationForm, LoginForm
from blog_package.models import User, Post

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
    return render_template("index.html", posts=posts, token="flask react")

@app.route('/about')
def renderAbout():
    return render_template("about.html")

@app.route("/register", methods=["GET", "POST"])
def renderRegister():
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
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You are logged in!", "success")
            return redirect(url_for("renderHomePage"))
        else:
            flash("Login unsuccessful. Please check username and/or password.", "danger")
    return render_template("login.html", title="Login", form=form)