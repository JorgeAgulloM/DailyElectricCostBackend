### MODEL -> SUBSCRIPTER ###

from typing import Optional
from pydantic import BaseModel
from domain.db.models.subscriptor import Subscriber

class SubscriberSrv(BaseModel):
    id: str = Optional[str] | None
    email: str
    activation_code: str = Optional[str] | None
    activated: bool = False
    date_activated: str = Optional[str] | None
    cancelated: bool = False
    date_cancelated: str = Optional[str] | None
    
def mapper_data_to_service(model: Subscriber) -> SubscriberSrv:
    subscriptor_srv: SubscriberSrv = model
    return subscriptor_srv

def mapper_service_to_data(model: SubscriberSrv) -> Subscriber:
    subscriber: Subscriber = model
    return subscriber
