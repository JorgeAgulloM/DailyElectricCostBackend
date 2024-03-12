### MODEL -> SUBSCRIPTER API ###

from typing import Optional
from pydantic import BaseModel
from service.subscriptions.models.subscripter import SubscriptorSrv

class SubscriptorApi(BaseModel):
    id: str = Optional[str] | None
    email: str
    activated: bool = False
    date_activated: str = Optional[str] | None
    cancelated: bool = False
    date_cancelated: str = Optional[str] | None
    

def mapper_service_to_api(model: SubscriptorSrv) -> SubscriptorApi:
    return SubscriptorApi(model.id, model.email, model.activated, model.date_activated, model.cancelated, model.date_cancelated)

def mapper_api_to_service(model: SubscriptorApi) -> SubscriptorSrv:
    return SubscriptorSrv(model.id, model.email, model.activated, model.date_activated, model.cancelated, model.date_cancelated)
