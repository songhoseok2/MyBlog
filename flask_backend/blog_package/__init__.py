from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

#TODO: Remember to remove this key then make and hide the new key after devlopment and before deploying
app.config["SECRET_KEY"] = "5cfbe6997170e10d89fe47aeca5d27a05c059a8c5408d36a3d501cf4356125b5"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from blog_package import routes