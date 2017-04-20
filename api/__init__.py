from flask_io import FlaskIO
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
io = FlaskIO()
ma = Marshmallow()
