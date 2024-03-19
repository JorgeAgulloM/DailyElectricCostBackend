### Service to send contact with developer ###

from domain.email.email_repository import send_email_contact_developer
from service.contact.model.contact import ContactSrv, mapper_model_to_DB

def contact_developer(contact: ContactSrv):
    send_email_contact_developer(mapper_model_to_DB(contact))
