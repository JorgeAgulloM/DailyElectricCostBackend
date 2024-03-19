### EMAIL SERVICE ###
from datetime import datetime
from bson import ObjectId

from domain.db.subscribes.subscribe_repository import search_subscribers, search_subscriber, insert, activate, cancel
from service.subscriptions.models.subscripter import SubscriberSrv, mapper_service_to_data
from domain.email.email_repository import send_email_verification 


def get_subscribers():
    return search_subscribers()


def insert_subscriber(subscriber: SubscriberSrv):
    new_subscriber = mapper_service_to_data(subscriber)
    
    # Search if email is suscripted
    email = new_subscriber.email
    subscriptor_exist = search_subscriber('email', email)

    if subscriptor_exist:
        if new_subscriber.activated:
            return {'warning': 'Este email ya está suscrito!'} #message to front
        else:
            return {'warning': 'Email ya suscrito pero no activado. Por favor, revise su correo.'} #message to front
    
    # Send and otain de activation code
    code = send_email_verification(email)
        
    # Insera al subscriptor en la DB
    new_subscriber.activation_code = code
    insert(mapper_service_to_data(new_subscriber))
    return {'message': 'Suscripción realizaca con éxito.\nRecivirá un email desde la dirección softYorch@outlook.es para verificar su email. Gracias!'} #message to front
    
    
def get_email(code: str):
    try:
        subscriber = search_subscriber('activation_code', code)
        if subscriber is None:
            return {
                'error': 'Ooops!! El correo a suscribir no existe.\n Prueba a realizar la subscripción de nuevo!',
                'error_message': 'Error: None type'  
            }
        return subscriber['email']
    except Exception as e:
        return {
            'error': 'Ooops!! Error al realizar la activación a la subscripción!',
            'error_message': f'Error: ${e}'    
        }
    

def activate_subscriber(code: str):
    try:
        subscriber = search_subscriber('activation_code', code)
        if subscriber is None:
            return {
                'error': 'Ooops!! El correo a suscribir no existe.\n Prueba a realizar la subscripción de nuevo!',
                'error_message': 'Error: None type'  
            }
        
        subscriber['date_activated'] = str(datetime.now())
        subscriber['activated'] = True
        subscriber['cancelated'] = False
        filter_id = {'_id': ObjectId(subscriber['_id'])}
    except Exception as e:
        return {
            'error': 'Ooops!! Error al realizar la activación a la subscripción!',
            'error_message': f'Error: ${e}'    
        }
    
    try:
        return activate(filter_id, subscriber)
    except Exception as e:
        return {
            'error': 'Ooops!! Error al realizar la activación a la subscripción!',
            'error_message': f'Error: ${e}'  
        }

def cancel_subscriber(code: str):
    try:
        subscriber = search_subscriber('activation_code', code)
        if subscriber is None:
            return {
                'error': 'Ooops!! El correo a cancelar no existe.\n Prueba de nuevo, si el error persiste, por favor, contacta con nosotros!',
                'error_message': 'Error: None type'  
            }
            
        subscriber['date_cancelated'] = str(datetime.now())
        subscriber['activated'] = False
        subscriber['cancelated'] = True
        
        filter_id = {'_id': ObjectId(subscriber['_id'])}
    except Exception as e:
        return {
            'error': 'Ooops!! Error al realizar la cancelación de tu subscripción!',
            'error_message': f'Error: ${e}'    
        }

    try:
        return cancel(filter_id, subscriber)
    except Exception as e:
        return {
            'error': 'Ooops!! Error al realizar la cancelación de tu subscripción!',
            'error_message': f'Error: ${e}'  
        }
