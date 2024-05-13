import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)

# fix compatibility issue between Windows and Unix-like systems
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
# login_manager.login_view = 'index'

@login_manager.user_loader
# user_loader callback to load a user by ID
def load_user(user_id):
    user = User.query.get(user_id)
    return user

from app import routes
from app.models import User