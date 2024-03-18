### EMAIL REPOSITORY ###
from fastapi import HTTPException, status
from typing import Any, Mapping

from data.db.subscribes.subscribe_db import db_find, db_find_one, db_insert_one, db_find_one_and_replace
from data.db.schemas.subscripter import subscripter_schema
from data.db.models.subscriptor import Subscriber, mapper_model_to_db

def search_subscribers():
    try:
        subscripters = subscripter_schema(db_find())
        if len(subscripters) == 0:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Don`t have subscripters!')
        return subscripters
    
    except Exception as e:
        return {
            'error': f'When getting subscripters! Error: {e}',
            'error_message': f'Error: ${e}'  
        }
    

def search_subscriber(field: str, key: str):
    try:
        return db_find_one(field, key)
    except Exception as e:
        return {'error': 'Ooops!! Error al realizar la activación a la subscripción!'}
    
    
def insert(subscriber: Subscriber):
    try:
        subscriber_dict = mapper_model_to_db(subscriber)
        db_insert_one(subscriber_dict)
    except Exception as e:
        return {'error': f'When inserting subscripter! Error: {e}'}
    

def activate(filter: Mapping[str, Any], replacement: Mapping[str, Any]):
    try:
        db_find_one_and_replace(filter, replacement)
        return {'message': 'Tu subscribción ha sido activada correctamente!'}
    except Exception as e:
        return {
            'error': 'Ooops!! Error al realizar la activación a la subscripción!',
            'error_message': f'Error: ${e}'      
        }      

def cancel(filter: Mapping[str, Any], replacement: Mapping[str, Any]):
    try:
        response = db_find_one_and_replace(filter, replacement)
        print(f'Response: {response}')
        return {'message': 'Tu subscribción ha sido cancelada correctamente.'}
    except Exception as e:
        return {
            'error': 'Ooops!! Error al realizar la cancelación de tu subscripción!',
            'error_message': f'Error: ${e}'      
        } 
        