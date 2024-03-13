### For Heroku enviroment ###

import os
from passlib.context import CryptContext

_dyno: str = 'DYNO'
_heroku: str = 'HEROKU'
_local: str = 'LOCAL'

# Configuration elastic email server
ELASTIC_EMAIL_SERVER = 'smtp.elasticemail.com'
ELASTIC_EMAIL_PORT = 2525

CRYPT = CryptContext(schemes='bcrypt')

if _dyno in os.environ:
    ENVIROMENT = _heroku
else:
    ENVIROMENT = _local

if ENVIROMENT == _heroku:

    # Token configuration
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_DURATION = 24 * 60
    SECRET = os.environ.get('SECRET')

    # DB Configuration
    name_db: str = os.environ.get('DATABASE_NAME')
    user_db: str = os.environ.get('DATABASE_USER')
    pass_db: str = os.environ.get('DATABASE_PASS')
    URL_DB: str = os.environ.get('URL_MONGO_DB')# = 'mongodb+srv://{}:{}@{}.mongodb.net/?retryWrites=true&w=majority'.format(user_db, pass_db, name_db)

    # Credentias SMTP for Elastic Email
    ELASTIC_EMAIL_USERNAME: str = os.environ.get('ELASTIC_EMAIL_USERNAME')
    ELASTIC_EMAIL_PASSWORD: str = os.environ.get('ELASTIC_EMAIL_PASSWORD')
    MAILTRAP_EMAIL_USERNAME: str = os.environ.get('MAILTRAP_EMAIL_USERNAME')
    MAILTRAP_EMAIL_PASSWORD: str = os.environ.get('MAILTRAP_EMAIL_PASSWORD')
else:
    from env import env_var as local
    
    # Token configuration
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_DURATION = 24 * 60
    SECRET = local.SECRET

    # DB Configuration
    URL_DB = local.URL_MONGO_DB

    # Credentias SMTP for Elastic Email
    ELASTIC_EMAIL_USERNAME = local.ELASTIC_EMAIL_USERNAME
    ELASTIC_EMAIL_PASSWORD = local.ELASTIC_EMAIL_PASSWORD
    MAILTRAP_EMAIL_USERNAME = local.MAILTRAP_EMAIL_USERNAME
    MAILTRAP_EMAIL_PASSWORD = local.MAILTRAP_EMAIL_PASSWORD
    