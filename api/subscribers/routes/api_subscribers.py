### Subscribers API ###

from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId

from api.subscribers.models.subscripter import SubscriberApi, mapper_api_to_service
from service.subscriptions.subscribe_service import get_subscribers, insert_subscriber, activate_subscriber, cancel_subscriber, get_email

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
@router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_new_subscriber(subscriber: SubscriberApi):
    return insert_subscriber(mapper_api_to_service(subscriber))


@router.get('/email/{code}')
def read_email(code: str):
    response = get_email(code)
    print(f'Email: {response}')
    return {'message': response}


""" Activate Suscriptor """
@router.get('/activate/{code}', status_code=status.HTTP_200_OK)
async def go_to_activate_subscriber(code: str):
    return activate_subscriber(code)


""" Cancel Subscription """
@router.get('/cancel/{code}', status_code=status.HTTP_200_OK)
async def cancel_subscription(code: str):
    return cancel_subscriber(code)
