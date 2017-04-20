import os
from api.application import create_app

ENV = os.environ.get('APP_ENV')

if not ENV:
    raise Exception('APP_ENV not found.')

application = create_app(ENV)
