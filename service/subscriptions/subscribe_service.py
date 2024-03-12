### EMAIL SERVICE ###
from datetime import datetime
from bson import ObjectId

from data.db.subscribes.subscribe_repository import search_subscribers, search_subscriber, insert, activate
from service.subscriptions.models.subscripter import SubscriberSrv, mapper_service_to_data
from data.email.email_repository import send_email_verification 


def get_subscribers():
    return search_subscribers()


def insert_subscriber(subscriptor: SubscriberSrv):
    
    # Search if email is suscripted
    email = subscriptor.email
    subscriptor_exist = search_subscriber('email', email)

    if subscriptor_exist:
        if subscriptor.activated:
            return {'error': 'Email suscripted'}
        else:
            return {'error': 'Email suscribed but not activated'}
    
    # Send and otain de activation code
    code = send_email_verification(email)
        
    # Insera al subscriptor en la DB
    edit_subscriber = subscriptor
    edit_subscriber.activation_code = code
    insert(mapper_service_to_data(edit_subscriber))
    

def activate_subscriber(code: str):
    try:
        subscriber = search_subscriber('code', code)
    except Exception as e:
        return {'error': f'When getting user. Error: {e}'}
    
    subscriber.date_activated = str(datetime.now())
    subscriber.activated = True
    filter_id = {'_id': ObjectId(subscriber.id)}
    
    try:
        return activate(filter_id, subscriber)
    except Exception as e:
        return {'error': f'When activating user. Error: {e}'}
