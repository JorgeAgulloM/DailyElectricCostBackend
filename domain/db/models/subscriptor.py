### MODEL -> SUBSCRIPTER ###

from typing import Optional
from pydantic import BaseModel

class Subscriber(BaseModel):
    id: str = Optional[str] | None
    email: str
    activation_code: str = Optional[str] | None
    activated: bool = False
    date_activated: str = Optional[str] | None
    cancelated: bool = False
    date_cancelated: str = Optional[str] | None
    
class SubscriberDB(BaseModel):
    id: str = ''
    email: str
    activation_code: str = ''
    activated: bool = False
    date_activated: str = ''
    cancelated: bool = False
    date_cancelated: str = ''
    
def mapper_model_to_db(model: Subscriber) -> dict:
    model_db = SubscriberDB(
        id=str(model.id or ''),  # Convertir a cadena de texto
        email=model.email,
        activation_code=str(model.activation_code or ''),  # Convertir a cadena de texto
        activated=model.activated,
        date_activated=str(model.date_activated or ''),  # Convertir a cadena de texto
        cancelated=model.cancelated,
        date_cancelated=str(model.date_cancelated or '')  # Convertir a cadena de texto
    )

    model_dict = model_db.dict()
    if 'id' in model_dict:
        del model_dict['id']
    return model_dict