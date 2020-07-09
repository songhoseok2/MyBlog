from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#TODO: Remember to remove this key then make and hide the new key after devlopment and before deploying
app.config["SECRET_KEY"] = "5cfbe6997170e10d89fe47aeca5d27a05c059a8c5408d36a3d501cf4356125b5"



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
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("renderHomePage"))
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



if __name__ == "__main__":
    app.run(debug=True)