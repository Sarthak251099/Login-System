from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, TextAreaField

class RegistrationForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password')
    weight = StringField('Weight')
    height = StringField('Height')
    gender = StringField('Gender')
    bloodgroup = StringField('Blood Group')
    DOB = StringField('Date of Birth')
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

