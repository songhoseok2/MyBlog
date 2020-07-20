from flask import render_template, request, Blueprint
from flask_login import login_user, current_user
from blog_package.models import Post
main = Blueprint("main", __name__)


@main.route('/')
def renderHomePage():
    page_to_access = request.args.get("page", 1, type=int)
    queried_all_posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page_to_access, per_page=5)
    return render_template("index.html", posts=queried_all_posts, is_logged_in=str(current_user.is_authenticated))


@main.route('/about')
def renderAbout():
    return render_template("about.html", is_logged_in=str(current_user.is_authenticated))




