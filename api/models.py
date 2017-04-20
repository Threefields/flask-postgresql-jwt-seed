from datetime import datetime

from . import db
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id                  = db.Column(db.Integer, primary_key=True)
    email               = db.Column(db.String(89), unique=True)
    password            = db.Column(db.String(255))
    last_login_at       = db.Column(db.DateTime())
    active              = db.Column(db.Boolean())
    current_login_at    = db.Column(db.DateTime())
    last_login_ip       = db.Column(db.String(255))
    current_login_ip    = db.Column(db.String(255))
    login_count         = db.Column(db.Integer)

class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id              = db.Column(db.Integer(), primary_key = True)
    name            = db.Column(db.String(80), unique = True)
    description     = db.Column(db.String(255))

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)
