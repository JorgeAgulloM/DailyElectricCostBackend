### Public API ###
from fastapi import APIRouter, status

from service.subscriptions.subscribe_service import activate_subscriber

router = APIRouter(
    prefix="/public/subscribers",
    tags=['public', 'subscribers'], 
    responses = {404: {'message': 'No encontrado'}}
)

""" Public Subscribes Ping """
@router.get("/ping")
def read_ping():
    return {'message': "subscribers pong"}


""" Activate Suscriptor """
@router.get('/activate/{code}', status_code=status.HTTP_200_OK)
async def go_to_activate_subscriber(code: str):
    activate_subscriber(code)
    return {'message': 'Email subscription has beenn activated'}


""" Cancel Subscription """
@router.get('/cancel/{code}', status_code=status.HTTP_200_OK)
async def cancel_subscription(code: str):
    return
