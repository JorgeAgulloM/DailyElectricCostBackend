### Email Service - Connexion to elasticemail.com ###

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from enviroment_config import URL_EMAIL_VERIFY, EMAIL_HTML_MESSAGE, ELASTIC_EMAIL_SERVER, ELASTIC_EMAIL_PORT, ELASTIC_EMAIL_USERNAME, ELASTIC_EMAIL_PASSWORD, OUTLOOK_EMAIL_SERVER, OUTLOOK_EMAIL_PORT, OUTLOOK_EMAIL_USERNAME, OUTLOOK_EMAIL_PASSWORD
from secrets import token_urlsafe


def send(recipient: str) -> str:
    # Crea el coódig
    code = _create_code()
    
    # Configura la url para la verificación
    url = _create_url(code)

    # Configura el correo electrónico
    sender = 'softyorch@outlook.es'
    message = EMAIL_HTML_MESSAGE(url)
    subject = 'DailyElectricCost.web.app Por favor, verifique su email.'

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

    return code

def _create_url(code: str) -> str:
    url = f"{URL_EMAIL_VERIFY}/activated_subscriber/{code}\n\n"
    print(url) #Solo para facilitar al activación del usuario.
    return url


def _create_code() -> str:
    code = token_urlsafe(32)
    return code
