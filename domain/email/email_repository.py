### Email Repository ###
from domain.email.email_service import send, send_contact
from domain.email.models.contact import ContactDB

def send_email_verification(recipient: str) -> str:
    return send(recipient)

def send_email_contact_developer(contact: ContactDB):
    send_contact(contact)
