from flask_io import fields, Schema, post_dump

from . import ma
from models import *

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

users_schema = UserSchema(many = True)
