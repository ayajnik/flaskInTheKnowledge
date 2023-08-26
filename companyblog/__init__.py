from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_login import LoginManager

###############################
######### app ################
##############################
app = Flask(__name__)

###############################
########## db #################
###############################

db = SQLAlchemy(app)
Migrate(app,db)
basedir = os.path.abspath(os.path.dirname(__name__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = False


################################
########### Login ##############
################################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

from companyblog.core.views import core
from companyblog.error_pages.views import error_handler

app.register_blueprint(core)
app.register_blueprint(error_handler)


