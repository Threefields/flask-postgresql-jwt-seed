from .. import db
from datetime import datetime

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
