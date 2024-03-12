### Email Repository ###
from data.email.email_service import send
from data.email.email_service_alt import send_email

def send_email_verification(recipient: str) -> str:
    return send_email(recipient)
