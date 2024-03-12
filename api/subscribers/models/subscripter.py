### MODEL -> SUBSCRIPTER API ###

from typing import Optional
from pydantic import BaseModel
from service.subscriptions.models.subscripter import SubscriberSrv

class SubscriberApi(BaseModel):
    id: str = Optional[str] | None
    email: str
    activation_code: str = Optional[str] | None
    activated: bool = False
    date_activated: str = Optional[str] | None
    cancelated: bool = False
    date_cancelated: str = Optional[str] | None
    

def mapper_service_to_api(model: SubscriberSrv) -> SubscriberApi:
    subscriber_api: SubscriberApi = model 
    return subscriber_api

def mapper_api_to_service(model: SubscriberApi) -> SubscriberSrv:
    subscribe_srv: SubscriberSrv = model
    return subscribe_srv
