import os
import logging

from flask import Flask
from flask_security import Security
from flask_security.utils import encrypt_password, verify_password
from flask_jwt import JWT, jwt_required, current_identity
from flask_sqlalchemy import SQLAlchemy

from . import db, ma
from models import *
from config import *

logger  = logging.getLogger(__name__)

def create_app(environment):

    config = {
        'production':   Production(),
        'development':  Development(),
        'testing':      Testing()
    }

    app = Flask(__name__)
    app.config.from_object(config[environment.lower()])
    app.url_map.strict_slashes = False

    # Routes
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/users', 'users', users)

    # Database Initialization
    db.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)

    # Flask-Security
    security = Security(app, user_datastore)

    # Flask-Marshmallow
    ma.init_app(app)

    return app

def authenticate(email, password):
    user = User.query.filter_by(email = email).first()
    if user and email == user.email and \
    verify_password(password, user.password):
            return user

    return None

def load_user(payload):
    user = user_datastore.find_user(id = payload['identity'])

    return user

def home():
    return  "TEST"

def users():
    users = User.query.all()
    result = users_schema.dump(users)

    return jsonify({'users': result.data})
