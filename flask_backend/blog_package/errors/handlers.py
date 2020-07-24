from flask import Blueprint, render_template
from flask_login import current_user
from blog_package import getCurrentUserJson
errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
def error_404_handler(error):
    return render_template("errors/404.html", **getCurrentUserJson(current_user)), 404


@errors.app_errorhandler(403)
def error_403_handler(error):
    return render_template("errors/403.html", **getCurrentUserJson(current_user)), 403


@errors.app_errorhandler(500)
def error_500_handler(error):
    return render_template("errors/500.html", **getCurrentUserJson(current_user)), 500
