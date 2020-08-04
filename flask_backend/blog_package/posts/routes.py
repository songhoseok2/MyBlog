from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from blog_package import db, getCurrentUserJson
from blog_package.models import Post, Comment, Anonymous_table
from blog_package.posts.forms import PostForm, CommentForm
posts = Blueprint("posts", __name__)


@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def makeNewPost():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user, is_anonymous=current_user.is_anonymous)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created.", "success")
        return redirect(url_for("main.renderHomePage"))

    return render_template("create_post.html", title="New Post", form=form, legend="New post", **getCurrentUserJson(current_user))


@posts.route("/post/<int:post_id>", methods=["GET", "POST"])
def renderPost(post_id):
    queried_post = Post.query.get_or_404(post_id)
    queried_comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.date_posted.asc())
    queried_anonymous_table = Anonymous_table.query.filter_by(post_id=post_id)
    queried_anonymous_table = queried_anonymous_table.all()
    anonymous_number_table = []

    for current_entry in queried_anonymous_table:
        anonymous_number_table.append({"user_id": current_entry.user_id,
                                       "number": current_entry.number})

    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(post_id=queried_post.id, content=form.content.data, commenter=current_user, is_anonymous=current_user.is_anonymous)
        db.session.add(comment)

        if current_user != queried_post.author and not Anonymous_table.query.filter_by(post_id=post_id, user_id=current_user.id).first():
            new_commenter_anonymous_number = Anonymous_table.query.filter_by(post_id=post_id).count()
            anonymous_number = Anonymous_table(post_id=post_id, user_id=current_user.id, number=new_commenter_anonymous_number)
            db.session.add(anonymous_number)

        db.session.commit()
        flash("Your comment has been created.", "success")
        return redirect(url_for("posts.renderPost", post_id=post_id))
    return render_template("post.html", title=queried_post.title, form=form, post=queried_post, comments=queried_comments.all(), anonymous_number_table=anonymous_number_table, **getCurrentUserJson(current_user))


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
    return render_template("create_post.html", title="New Post", form=form, legend="Update post", **getCurrentUserJson(current_user))


@posts.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def deletePost(post_id):
    queried_post = Post.query.get_or_404(post_id)
    if queried_post.author != current_user:
        abort(403)
    db.session.delete(queried_post)

    queried_comments = Comment.query.filter_by(post_id=post_id)
    queried_anonymous_tables = Anonymous_table.query.filter_by(post_id=post_id)

    for comment in queried_comments:
        db.session.delete(comment)
    for anonymous_table in queried_anonymous_tables:
        db.session.delete(anonymous_table)

    db.session.commit()
    flash("Your post was deleted.", "success")
    return redirect(url_for("main.renderHomePage"))


@posts.route("/post/<int:post_id>/identity_change", methods=["GET", "POST"])
@login_required
def changePostIdentity(post_id):
    queried_post = Post.query.get_or_404(post_id)
    queried_post.is_anonymous = not queried_post.is_anonymous
    db.session.commit()
    return redirect(url_for("posts.renderPost", post_id=post_id))


@posts.route("/post/<int:post_id>/<int:comment_id>/identity_change", methods=["GET", "POST"])
@login_required
def changeCommentIdentity(post_id, comment_id):
    queried_comment = Comment.query.get_or_404(comment_id)
    queried_comment.is_anonymous = not queried_comment.is_anonymous
    db.session.commit()
    return redirect(url_for("posts.renderPost", post_id=post_id))


@posts.route("/comment/<int:post_id>/<int:comment_id>/update", methods=["GET", "POST"])
@login_required
def updateComment(post_id, comment_id):
    queried_comment = Comment.query.get_or_404(comment_id)
    if queried_comment.commenter != current_user:
        abort(403)
    form = CommentForm()

    if form.validate_on_submit():
        queried_comment.content = form.content.data
        db.session.commit()
        flash("Your comment has been updated.", "success")
        return redirect(url_for("posts.renderPost", post_id=post_id))
    elif request.method == "GET":
        form.content.data = queried_comment.content

    form.content.data = queried_comment.content
    return render_template("update_comment.html", title="Update Comment", form=form, legend="Update comment", **getCurrentUserJson(current_user))


@posts.route("/post/<int:post_id>/<int:comment_id>/delete", methods=["POST"])
@login_required
def deleteComment(post_id, comment_id):
    queried_comment = Comment.query.get_or_404(comment_id)
    if queried_comment.commenter != current_user:
        abort(403)
    db.session.delete(queried_comment)
    db.session.commit()
    flash("Your comment was deleted.", "success")
    return redirect(url_for("posts.renderPost", post_id=post_id))




