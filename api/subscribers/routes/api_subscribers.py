### Subscribers API ###

from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId

from api.subscribers.models.subscripter import SubscriberApi
from service.subscriptions.subscribe_service import get_subscribers, insert_subscriber, activate_subscriber

router = APIRouter(
    prefix="/subscribers",
    tags=['subscribers'], 
    responses = {404: {'message': 'No encontrado'}}
)

#####################################################################################################################
########################################### API CRUD Susbscripters ##################################################
#####################################################################################################################


""" Subscribe ping """
@router.get('/ping')
async def ping():
    return {'response': 'pong'}

""" Get Subscribers """
@router.get('/', response_model=list[SubscriberApi], status_code=status.HTTP_200_OK)
async def get_subscriber_list():
    print('get subscribers')
    return get_subscribers()


""" Insert subscribers """
@router.post('/{email}', status_code=status.HTTP_201_CREATED)
async def insert_new_subscriber(email: str):
    return insert_subscriber(email)


""" Activate Suscriptor """
@router.put('/activated_subscriber/{code}', status_code=status.HTTP_200_OK)
async def go_to_activate_subscriber(code: str):
    activate_subscriber(code)
    return {'message': 'Activated'}


""" Cancel Subscription """
@router.put('/cancel_subscriber/{email}', status_code=status.HTTP_200_OK)
async def cancel_subscription(email: str):
    return

