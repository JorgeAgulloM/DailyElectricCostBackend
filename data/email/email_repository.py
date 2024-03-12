### Email Repository ###
from data.email.email_service import send, _create_code, create_url

def send_email_verification(recipient: str):
    send(recipient)
