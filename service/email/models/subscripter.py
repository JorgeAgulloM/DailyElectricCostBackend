### MODEL -> SUBSCRIPTER ###

from typing import Optional
from pydantic import BaseModel
from data.db.models.subscripter import Subscriptor

class SubscriptorSrv(BaseModel):
    id: str = Optional[str] | None
    email: str
    activated: bool = False
    date_activated: str = Optional[str] | None
    cancelated: bool = False
    date_cancelated: str = Optional[str] | None
    
    
def mapper_data_to_service(data: Subscriptor) -> SubscriptorSrv:
    return SubscriptorSrv(data.id, data.email, data.activated, data.date_activated, data.cancelated, data.date_cancelated)    

def mapper_service_to_data(data: SubscriptorSrv) -> Subscriptor:
    return Subscriptor(data.id, data.email, data.activated, data.date_activated, data.cancelated, data.date_cancelated)
