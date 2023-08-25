from flask import Flask, render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, TextAreaField
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
import os

## initializing the app, db
app = Flask(__name__)


## setting the congif for forms and db

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'mysecretkeylogin'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## initialize the migration

Migrate(app,db)

##setting up the login app

## initialize the app
login_manager=LoginManager()

login_manager.init_app(app)

## what view we want to render when the login is completed
login_manager.login_view = "login"