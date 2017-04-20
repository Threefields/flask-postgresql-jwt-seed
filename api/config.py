import os
from datetime import timedelta

class Config(object):
    DB_HOST                         = os.environ.get('DB_HOST') or 'localhost'
    DB_USERNAME                     = os.environ.get('DB_USERNAME')
    DB_PASSWORD                     = os.environ.get('DB_PASSWORD')

    DEBUG                           = False
    TESTING                         = False
    SECRET_KEY                      = os.environ.get('SECRET_KEY')
    JWT_EXPIRATION_DELTA            = timedelta(days=30)
    SECURITY_TRACKABLE              = True
    SECURITY_PASSWORD_HASH          = 'sha512_crypt'
    SECURITY_PASSWORD_SALT          = 'add_salt'
    JWT_AUTH_URL_RULE               = '/user/login'
    JWT_AUTH_USERNAME_KEY           = 'email'
    SQLALCHEMY_TRACK_MODIFICATIONS  = False

class Production(Config):
    SQLALCHEMY_DATABASE_URI         = 'postgresql://username:password@host'

class Development(Config):
    DEBUG                           = True
    SQLALCHEMY_DATABASE_URI         = 'postgresql://username:password@host'

class Testing(Config):
    TESTING                         = True
    SQLALCHEMY_DATABASE_URI         = 'postgresql://username:password@host'
