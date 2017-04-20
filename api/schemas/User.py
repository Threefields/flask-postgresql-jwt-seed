from .. import ma
from flask_io import fields, Schema, post_dump
from models import User

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
