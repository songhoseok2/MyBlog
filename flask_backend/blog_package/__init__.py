import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

cur_path = os.path.dirname(__file__)
secret_key_file = open(cur_path + "/private_variables/secret_key.txt", 'r')
app.config["SECRET_KEY"] = secret_key_file.read()
secret_key_file.close()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "users.renderLogin"
login_manager.login_message_category = "info"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True

email_address_file = open(cur_path + "/private_variables/email_address.txt", 'r')
email_password_file = open(cur_path + "/private_variables/email_password.txt", 'r')
app.config["MAIL_USERNAME"] = email_address_file.read()
app.config["MAIL_PASSWORD"] = email_password_file.read()
email_address_file.close()
email_password_file.close()

mail = Mail(app)

from blog_package.users.routes import users
from blog_package.posts.routes import posts
from blog_package.main.routes import main
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

