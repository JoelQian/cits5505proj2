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

# 设置测试模式
app.config['TESTING'] = True  # 在测试时设置为True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'
db = SQLAlchemy(app)

# 设置数据库URI
if app.config['TESTING']:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # 使用内存数据库
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(basedir, 'app.db')


login_manager = LoginManager(app)
# login_manager.login_view = 'index'

@login_manager.user_loader
# user_loader callback to load a user by ID
def load_user(user_id):
    user = User.query.get(user_id)
    return user

from app import routes
from app.models import User
