### Email Service - Connexion to elasticemail.com ###

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from enviroment_config import ELASTIC_EMAIL_SERVER, ELASTIC_EMAIL_PORT, ELASTIC_EMAIL_USERNAME, ELASTIC_EMAIL_PASSWORD
from secrets import token_urlsafe


def send(recipient: str) -> str:
    # Crea el coódig
    code = _create_code()
    
    # Configura la url para la verificación
    url = _create_url(code)

    # Configura el correo electrónico
    sender = 'agullojorge@gmail.com'
    message = f'Probando el envio de correos\n\n{url}'
    subject = 'Por favor, verifique su Email.'

    # Crea el mensaje
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    # Agrega el cuerpo del correo
    msg.attach(MIMEText(message, 'plain'))

    # Inicia la conexión SMTP
    smtp = SMTP(ELASTIC_EMAIL_SERVER, ELASTIC_EMAIL_PORT)
    smtp.starttls()  # Habilita TLS si es necesario

    # Inicia sesión con tus credenciales
    smtp.login(ELASTIC_EMAIL_USERNAME, ELASTIC_EMAIL_PASSWORD)

    # Envía el correo electrónico
    smtp.sendmail(sender, recipient, msg.as_string())

    # Cierra la conexión SMTP
    smtp.quit()

    return code

def _create_url(code: str) -> str:
    url = f"http://127.0.0.1:8000/login/verify_email/{code}\n\n"
    print(url) #Solo para facilitar al activación del usuario.
    return url


def _create_code() -> str:
    code = token_urlsafe(32)
    return code
