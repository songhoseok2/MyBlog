import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from blog_package import mail


def savePicture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_fn)
    output_size = (125, 125)
    resized_img = Image.open(form_picture)
    resized_img.thumbnail(output_size)
    resized_img.save(picture_path)
    return picture_fn


def sendResetEmail(user):
    token = user.get_reset_token()
    msg = Message("Password Reset Request", sender=app.config["MAIL_USERNAME"], recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link: 
    {url_for("users.renderResetToken", token=token, _external=True)}
    If you did not make this request then simply ignore this email and no change will be made
    '''
    mail.send(msg)





