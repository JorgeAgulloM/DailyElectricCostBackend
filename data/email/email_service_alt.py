import smtplib

from enviroment_config import MAILTRAP_EMAIL_USERNAME, MAILTRAP_EMAIL_PASSWORD


def send_email(receiver: str):

    sender = "info@softyorch.com"
    #receiver = "A Test User <to@example.com>"

    message = f"""\
    Subject: Hola
    To: {receiver}
    From: {sender}

    This is a test e-mail message."""

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.login(MAILTRAP_EMAIL_USERNAME, MAILTRAP_EMAIL_PASSWORD)
        server.sendmail(sender, receiver, message)