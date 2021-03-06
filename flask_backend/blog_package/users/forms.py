
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from blog_package.models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username_to_validate):
        user = User.query.filter_by(username=username_to_validate.data).first()
        if user:
            raise ValidationError("\"" + username_to_validate.data + "\" is already taken. Please choose a different username." )
    
    def validate_email(self, email_to_validate):
        user = User.query.filter_by(email=email_to_validate.data).first()
        if user:
            raise ValidationError("\"" + email_to_validate.data + "\" is already registered. Please choose a different email." )


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture = FileField("Update profile picture", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Update")

    def validate_username(self, username_to_validate):
        if username_to_validate.data != current_user.username:
            user = User.query.filter_by(username=username_to_validate.data).first()
            if user:
                raise ValidationError("\"" + username_to_validate.data + "\" is already taken. Please choose a different username." )
    
    def validate_email(self, email_to_validate):
         if email_to_validate.data != current_user.email:
            user = User.query.filter_by(email=email_to_validate.data).first()
            if user:
                raise ValidationError("\"" + email_to_validate.data + "\" is already taken. Please choose a different username." )


class RequestResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Request password reset")

    def validate_email(self, email_to_validate):
        user = User.query.filter_by(email=email_to_validate.data).first()
        if user is None:
            raise ValidationError("\"" + email_to_validate.data + "\" is not a registered account. You must register first." )
        

class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Reset password")


