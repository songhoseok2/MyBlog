import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)




f = open("../private_variables/secret_key.txt", 'r')
app.config["SECRET_KEY"] = f.read()
f.close()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "renderLogin"
login_manager.login_message_category = "info"
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
f2 = open("../private_variables/email_address.txt", 'r')
f3 = open("../private_variables/email_password.txt", 'r')
app.config["MAIL_USERNAME"] = f2.read()
app.config["MAIL_PASSWORD"] = f3.read()
f2.close()
f3.close()

mail = Mail(app)

from blog_package import routes
