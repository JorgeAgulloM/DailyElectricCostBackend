### Email Service - Connexion to elasticemail.com ###

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from enviroment_config import URL_EMAIL_VERIFY, ELASTIC_EMAIL_SERVER, ELASTIC_EMAIL_PORT, ELASTIC_EMAIL_USERNAME, ELASTIC_EMAIL_PASSWORD, OUTLOOK_EMAIL_SERVER, OUTLOOK_EMAIL_PORT, OUTLOOK_EMAIL_USERNAME, OUTLOOK_EMAIL_PASSWORD
from secrets import token_urlsafe
from data.email.models.contact import ContactDB


def send_contact(contact: ContactDB):
    recipient = 'softyorch@outlook.es'
    message = _html_email_contact(contact)
    subject = f'Enviado desde DailyElectricCost: {contact.name}'
    
    _sender_builder(recipient, subject, message)


def send(recipient: str) -> str:
    # Crea el coódig
    code = _create_code()
    
    # Configura la url para la verificación
    url = _create_url(code)

    # Configura el correo electrónico
    message = _html_email_message(url)
    subject = 'DailyElectricCost.web.app Por favor, verifique su email.'

    _sender_builder(recipient, subject, message)
    
    return code


def _sender_builder(recipient, subject, message):
    # Configura el correo electrónico
    sender = 'softyorch@outlook.es'
    
    # Crea el mensaje
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    
    # Agrega el cuerpo del correo
    msg.attach(MIMEText(message, 'html'))

    # Inicia la conexión SMTP
    smtp = SMTP(OUTLOOK_EMAIL_SERVER, OUTLOOK_EMAIL_PORT)
    smtp.starttls()  # Habilita TLS si es necesario

    # Inicia sesión con tus credenciales
    smtp.login(OUTLOOK_EMAIL_USERNAME, OUTLOOK_EMAIL_PASSWORD)

    # Envía el correo electrónico
    smtp.sendmail(sender, recipient, msg.as_string())

    # Cierra la conexión SMTP
    smtp.quit()


def _create_url(code: str) -> str:
    url = f"{URL_EMAIL_VERIFY}/{code}\n\n"
    return url


def _create_code() -> str:
    code = token_urlsafe(32)
    return code


def _html_email_contact(contact: ContactDB) -> str:
    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contacto</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
            }}
            .email-content {{
                background-color: #f4f4f4;
                padding: 20px;
                border-radius: 5px;
                margin-bottom: 20px;
            }}
            .user-email {{
                font-weight: bold;
                color: #333;
            }}
        </style>
        </head>
        <body>

        <div class="email-content">
        <p>Usuario: {contact.name}</p>
        <p class="user-email">Email: {contact.email}</p>
        <br>
        <p>{contact.content}</p>
        </div>

        </body>
        </html>
    """


def _html_email_message(url: str) -> str: 
    return f"""
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
            <img src="https://raw.githubusercontent.com/JorgeAgulloM/DailyElectricCostBackend/main/assets/bombilla_hi.png" alt="Cabecera" class="header-img">
            <h2>¡Confirmación de Suscripción!</h2>
            <p>Estimado/a usuario/a,</p>
            <p>Hemos recibido su solicitud de suscripción a <strong>DailyElectricCost.web.app</strong>, su app de confianza para información sobre costos energéticos y optimización de consumo eléctrico.</p>
            <p>Por favor, complete el proceso de suscripción haciendo clic en el enlace a continuación:</p>
            <p><a href="{url}" target="_blank">Verificar Suscripción</a></p>
            <p>Para obenter más información sobre el coste eléctrico en España, descargue nuestra app desde <a href="https://play.google.com/store/apps/details?id=com.softyorch.dailyelectriccost" target="_blank">Google Play!</a></p>
            <p>¡Gracias por confiar en nosotros!</p>
            <p>Atentamente,<br>El Equipo de DailyElectricCost</p>
        </div>
        </body>
        </html>
        """