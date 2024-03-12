### EMAIL SERVICE ###
from data.db.subscribes.subscribe_repository import search_subscripters, insert_subscription
from service.subscriptions.models.subscripter import SubscriptorSrv, mapper_service_to_data
from data.email.email_repository import send_email_verification 


def get_subscriptors():
    return search_subscripters()


def insert_subscriptor(subscriptor: SubscriptorSrv):
    # Insera al subscriptor en la DB
    result = insert_subscription(mapper_service_to_data(subscriptor))
    
    # Si no hay error en la inserción, se genera y envia el correo de verificación.
    if 'error' not in result:
        email = subscriptor.email
        return send_email_verification(email)
    
    return result

