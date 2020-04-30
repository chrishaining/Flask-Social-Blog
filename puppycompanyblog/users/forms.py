from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from puppycompanyblog.models import User

##################
### Login form ###
##################
class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Enter your password', validators = [DataRequired()])
    submit = SubmitField('Login')

#########################
### Registration form ###
#########################
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])

    username = StringField('Username', validators = [DataRequired()])

    password = PasswordField('Enter your password', validators = [DataRequired(), EqualTo('password_confirm', message='Passwords must match')])

    password_confirm = PasswordField('Confirm your password', validators=[DataRequired()])

    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email has already been used')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
                raise ValidationError('This username has already been used')

#######################
### UpdateUser form ###
#######################
class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])

    username = StringField('Username', validators = [DataRequired()])

    picture = FileField('Update your profile picture', validators = [FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email has already been used')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
                raise ValidationError('This username has already been used')
