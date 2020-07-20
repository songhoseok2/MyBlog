from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from blog_package import db
from blog_package.models import Post
from blog_package.posts.forms import PostForm
posts = Blueprint("posts", __name__)


@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def makeNewPost():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created.", "success")
        return redirect(url_for("main.renderHomePage"))

    return render_template("create_post.html", title="New Post", form=form, legend="New post", is_logged_in=str(current_user.is_authenticated))


@posts.route("/post/<int:post_id>")
def renderPost(post_id):
    queried_post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=queried_post.title, post=queried_post, is_logged_in=str(current_user.is_authenticated))


@posts.route("/post/<int:post_id>/update", methods=["GET", "POST"])
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
        return redirect(url_for("posts.renderPost", post_id=queried_post.id))
    elif request.method == "GET":
        form.title.data = queried_post.title
        form.content.data = queried_post.content

    form.title.data = queried_post.title
    form.content.data = queried_post.content
    return render_template("create_post.html", title="New Post", form=form, legend="Update post", is_logged_in=str(current_user.is_authenticated))


@posts.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def deletePost(post_id):
    queried_post = Post.query.get_or_404(post_id)
    if queried_post.author != current_user:
        abort(403)
    db.session.delete(queried_post)
    db.session.commit()
    flash("Your post was deleted.", "success")
    return redirect(url_for("main.renderHomePage"))

