from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, TextAreaField

class RegisterDoc(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password', )
    confirm_password = PasswordField('Confirm Password')
    specialization = StringField('Specialization')
    degree = StringField('Degree')
    phonenumber = StringField('Phone Number')
    address = StringField('Address')
    submit = SubmitField('Sign Up')


