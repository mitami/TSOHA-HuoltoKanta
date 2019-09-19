from flask import Flask
app = Flask(__name__)
app.static_folder = 'static'

from flask_sqlalchemy import SQLAlchemy

import os
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///konekanta.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views
from application.models import action, executor, location, target
from application.controllers import executor, action, location, target, login
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from application.models.executor import Executor
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "user_login"
login_manager.login_message = "You need to be logged in to access this resource."

@login_manager.user_loader
def load_user(executor_id):
    return Executor.query.get(executor_id)

db.create_all()