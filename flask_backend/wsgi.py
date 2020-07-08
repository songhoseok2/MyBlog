from flask import Flask, render_template, url_for, jsonify
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

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

@app.route("/register")
def register():
    form = RegistrationForm()
    print("DEBUG: form:", form, flush=True)
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)



if __name__ == "__main__":
    app.run(debug=True)