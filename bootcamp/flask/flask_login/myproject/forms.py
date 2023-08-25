from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import validators

class LoginForm(FlaskForm):
    username = StringField('Username:',validators=[DataRequired()])
    password=PasswordField('Password:',validators=[DataRequired()])
    submitfield = SubmitField('Submit',validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    email=StringField('Email Address:', validators=[DataRequired()])
    username=StringField('Username:',validators=[DataRequired()])
    password=PasswordField('Password:',validators=[DataRequired()])
    confirm_pass=PasswordField('Confirm Password:',validators=[DataRequired(),EqualTo('pass_confirm', message='Passwords Must Match!')])