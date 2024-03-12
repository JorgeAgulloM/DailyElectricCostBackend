### Subscripters API ###

from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId

from api.subscripters.models.subscripter import SubscriptorApi
from service.subscriptions.subscribe_service import get_subscriptors, insert_subscriptor

router = APIRouter(
    prefix="/subscripters",
    tags=['subscripters'], 
    responses = {404: {'message': 'No encontrado'}}
)

#####################################################################################################################
########################################### API CRUD Susbscripters ##################################################
#####################################################################################################################

""" Get Subscripters """
@router.get('/', response_model=list(SubscriptorApi), status_code=status.HTTP_200_OK)
async def get_subscripters():
    return get_subscriptors()


""" Insert Subscripter """
@router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_new_subscriptor(email: str):
    new_subscriptor = SubscriptorApi(email = email)
    response = insert_subscriptor(new_subscriptor)
    return response


""" Activate Suscriptor """
@router.post('/', status_code=status.HTTP_200_OK)
async def activate_subscriptors(code: str):
    return


""" Cancel Subscription """
@router.post('/', status_code=status.HTTP_200_OK)
async def cancel_subscription(email: str):
    return

