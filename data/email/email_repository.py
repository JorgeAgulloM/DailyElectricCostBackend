### Email Repository ###
from data.email.email_service import send

def send_email_verification(recipient: str) -> str:
    return send(recipient)
