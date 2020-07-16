import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from blog_package import app, db, bcrypt
from blog_package.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from blog_package.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def renderHomePage():
    page_to_access = request.args.get("page", 1, type=int)
    queried_all_posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page_to_access, per_page=5)
    return render_template("index.html", posts=queried_all_posts, is_logged_in=str(current_user.is_authenticated))


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
    output_size = (125, 125)
    resized_img = Image.open(form_picture)
    resized_img.thumbnail(output_size)
    resized_img.save(picture_path)
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
    return render_template("account.html", title="Account", image_file=image_file, form=form, is_logged_in=str(current_user.is_authenticated))


@app.route("/post/new", methods=["GET", "POST"])
@login_required
def makeNewPost():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created.", "success")
        return redirect(url_for("renderHomePage"))

    return render_template("create_post.html", title="New Post", form=form, legend="New post", is_logged_in=str(current_user.is_authenticated))


@app.route("/post/<int:post_id>")
def renderPost(post_id):
    queried_post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=queried_post.title, post=queried_post, is_logged_in=str(current_user.is_authenticated))


@app.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def updatePost(post_id):
    queried_post = Post.query.get_or_404(post_id)
    if queried_post.author != current_user:
        abort(403)
    form = PostForm()

    if form.validate_on_submit():
        queried_post.title = form.title.data
        queried_post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated.", "success")
        return redirect(url_for("renderPost", post_id=queried_post.id))
    elif request.method == "GET":
        form.title.data = queried_post.title
        form.content.data = queried_post.content

    form.title.data = queried_post.title
    form.content.data = queried_post.content
    return render_template("create_post.html", title="New Post", form=form, legend="Update post", is_logged_in=str(current_user.is_authenticated))

@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def deletePost(post_id):
    queried_post = Post.query.get_or_404(post_id)
    if queried_post.author != current_user:
        abort(403)
    db.session.delete(queried_post)
    db.session.commit()
    flash("Your post was deleted.", "success")
    return redirect(url_for("renderHomePage"))


@app.route("/user/<string:selected_username>")
def renderUserPosts(selected_username):
    page_to_access = request.args.get("page", 1, type=int)
    selected_user = User.query.filter_by(username=selected_username).first_or_404()
    queried_user_posts = Post.query.filter_by(author=selected_user).order_by(Post.date_posted.desc()).paginate(page=page_to_access, per_page=5)
    return render_template("user_posts.html", posts=queried_user_posts, user=selected_user, is_logged_in=str(current_user.is_authenticated))




