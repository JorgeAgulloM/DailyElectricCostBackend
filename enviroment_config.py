### For Heroku enviroment ###

import os
from passlib.context import CryptContext

_dyno: str = 'DYNO'
_heroku: str = 'HEROKU'
_local: str = 'LOCAL'

# Configuration elastic email server
ELASTIC_EMAIL_SERVER = 'smtp.elasticemail.com'
ELASTIC_EMAIL_PORT = 2525

# Configuration outlook email server
OUTLOOK_EMAIL_SERVER = 'smtp-mail.outlook.com'
OUTLOOK_EMAIL_PORT = 587

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
    
    # Url for email verify
    URL_EMAIL_VERIFY: str = 'https://daily-electric-cost-bakend-8028a574d40e.herokuapp.com' 

    # Credentias SMTP for Elastic Email
    ELASTIC_EMAIL_USERNAME: str = os.environ.get('ELASTIC_EMAIL_USERNAME')
    ELASTIC_EMAIL_PASSWORD: str = os.environ.get('ELASTIC_EMAIL_PASSWORD')

    # Credentias SMTP for Outlook Email
    OUTLOOK_EMAIL_USERNAME: str = os.environ.get('OUTLOOK_EMAIL_USERNAME')
    OUTLOOK_EMAIL_PASSWORD: str = os.environ.get('OUTLOOK_EMAIL_PASSWORD')
    
else:
    from env import env_var as local
    
    # Token configuration
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_DURATION = 24 * 60
    SECRET = local.SECRET

    # DB Configuration
    URL_DB = local.URL_MONGO_DB
    
    # Url for email verify
    URL_EMAIL_VERIFY: str = 'http://127.0.0.1:8000' 

    # Credentias SMTP for Elastic Email
    ELASTIC_EMAIL_USERNAME: str = local.ELASTIC_EMAIL_USERNAME
    ELASTIC_EMAIL_PASSWORD: str = local.ELASTIC_EMAIL_PASSWORD

    # Credentias SMTP for Outlook Email
    OUTLOOK_EMAIL_USERNAME: str = local.OUTLOOK_EMAIL_USERNAME
    OUTLOOK_EMAIL_PASSWORD: str = local.OUTLOOK_EMAIL_PASSWORD
    
def EMAIL_HTML_MESSAGE(url: str): return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirmación de Suscripción - DailyElectricCost</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        h2 {{
            color: #333333;
        }}
        p {{
            color: #666666;
            margin-bottom: 20px;
        }}
        a {{
            color: #007bff;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .header-img {{
            width: 100%;
            max-width: 200px;
            height: auto;
            margin-bottom: 20px;
        }}
    </style>
    </head>
    <body>
    <div class="container">
        <img src="{URL_EMAIL_VERIFY}/assets/bombilla_hi.png" alt="Cabecera" class="header-img">
        <h2>¡Confirmación de Suscripción!</h2>
        <p>Estimado/a usuario/a,</p>
        <p>Hemos recibido su solicitud de suscripción a <strong>DailyElectricCost.web.app</strong>, su app de confianza para información sobre costos energéticos y optimización de consumo eléctrico.</p>
        <p>Por favor, complete el proceso de suscripción haciendo clic en el enlace a continuación:</p>
        <p><a href="{url}" target="_blank">Verificar Suscripción</a></p>
        <p>¡Gracias por confiar en nosotros!</p>
        <p>Atentamente,<br>El Equipo de DailyElectricCost</p>
    </div>
    </body>
    </html>
    """