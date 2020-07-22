
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from blog_package import db, bcrypt
from blog_package.models import User, Post
from blog_package.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from blog_package.users.utils import savePicture, sendResetEmail
users = Blueprint('users', __name__)


@users.route("/register", methods=["GET", "POST"])
def renderRegister():
    if current_user.is_authenticated:
        return redirect(url_for("main.renderHomePage"))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("main.renderLogin"))
    return render_template("register.html", title="Register", form=form, logged_in_user=str(current_user.username))


@users.route("/login", methods=["GET", "POST"])
def renderLogin():
    if current_user.is_authenticated:
        return redirect(url_for("main.renderHomePage"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.renderHomePage"))
        else:
            flash("Login unsuccessful. Please check email and/or password.", "danger")
    return render_template("login.html", title="Login", form=form, logged_in_user=str(current_user.username))


@users.route("/logout")
def renderLogout():
    logout_user()
    return redirect(url_for("main.renderHomePage"))


@users.route("/account",  methods=["GET", "POST"])
@login_required
def renderAccount():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = savePicture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated.", "success")
        return redirect(url_for("users.renderAccount"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("account.html", title="Account", image_file=image_file, form=form, logged_in_user=str(current_user.username))


@users.route("/user/<string:selected_username>")
def renderUserPosts(selected_username):
    if selected_username == '-':
        flash("Please log in to view your posts.", "info")
        return redirect(url_for("users.renderLogin"))
    page_to_access = request.args.get("page", 1, type=int)
    selected_user = User.query.filter_by(username=selected_username).first_or_404()
    queried_user_posts = Post.query.filter_by(author=selected_user).order_by(Post.date_posted.desc()).paginate(page=page_to_access, per_page=5)
    return render_template("user_posts.html", posts=queried_user_posts, user=selected_user, logged_in_username=str(current_user.username))


@users.route("/reset_password", methods=["GET", "POST"])
def renderResetRequest():
    if current_user.is_authenticated:
        return redirect(url_for("main.renderHomePage"))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        sendResetEmail(user)
        flash("An email has been sent with instructions to reset your password. If you don't see any mail in your inbox, please check your spams folder.", "info")
        return redirect(url_for("users.renderLogin"))
    return render_template("reset_request.html", title="Reset Password", form=form, logged_in_username=str(current_user.username))


@users.route("/reset_password/<token>", methods=["GET", "POST"])
def renderResetToken(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.renderHomePage"))
    user = User.verify_reset_token(token)
    if user is None:
        flash("That is an invalid or expired token", "warning")
        return redirect(url_for("users.renderResetRequest"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user.password = hashed_password
        db.session.commit()
        flash(f"Your password has been updated.", "success")
        return redirect(url_for("users.renderLogin"))
    return render_template("reset_token.html", title="Reset Password", form=form, logged_in_username=str(current_user.username))

