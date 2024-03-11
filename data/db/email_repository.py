### EMAIL REPOSITORY ###
from fastapi import HTTPException, status
from datetime import datetime

from data.db.email_db import db_find, db_insert_one
from data.db.schemas.subscripter import subscripter_schema
from data.db.models.subscripter import Subscriptor

def search_subscripters():
    try:
        subscripters = subscripter_schema(db_find())
        if len(subscripters) == 0:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Don`t have subscripters!')
        return subscripters
    
    except Exception as e:
        return {'error': f'When getting subscripters! Error: {e}'}
    
def insert_subscription(subscriptor: Subscriptor):
    try:
        subscriptor.date_activated = str(datetime.now())
        
        result = db_insert_one(subscriptor)
        return result
    except Exception as e:
        return {'error': f'When inserting subscripter! Error: {e}'}