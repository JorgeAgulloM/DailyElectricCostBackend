### For Heroku enviroment ###

import os
from passlib.context import CryptContext

from secrets import env_var as local

_dino: str = 'DINO'
_heroku: str = 'HEROKU'
_local: str = 'LOCAL'

# Configuration elastic email server
ELASTIC_EMAIL_SERVER = 'smtp.elasticemail.com'
ELASTIC_EMAIL_PORT = 2525

CRYPT = CryptContext(schemes='bcrypt')

if _dino in os.environ:
    ENVIROMENT = _heroku
else:
    ENVIROMENT = _local

if _heroku == _local:

    # Token configuration
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_DURATION = 5
    SECRET = os.environ.get('SECRET')

    # DB Configuration
    name_db: str = os.environ.get('DATABASE_NAME')
    user_db: str = os.environ.get('DATABASE_USER')
    pass_db: str = os.environ.get('DATABASE_PASS')
    URL_DB = 'mongodb+srv://{}:{}@{}.mongodb.net/?retryWrites=true&w=majority'.format(user_db, pass_db, name_db)

    # Credentias SMTP for Elastic Email
    ELASTIC_EMAIL_USERNAME: str = os.environ.get('ELASTIC_EMAIL_USERNAME')
    ELASTIC_EMAIL_PASSWORD: str = os.environ.get('ELASTIC_EMAIL_PASSWORD')
else:

    # Token configuration
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_DURATION = 24 * 60
    SECRET = local.SECRET

    # DB Configuration
    URL_DB = local.URL_MONGO_DB

    # Credentias SMTP for Elastic Email
    ELASTIC_EMAIL_USERNAME = local.ELASTIC_EMAIL_USERNAME
    ELASTIC_EMAIL_PASSWORD = local.ELASTIC_EMAIL_PASSWORD
