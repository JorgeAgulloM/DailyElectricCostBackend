### Model Data For Contact to Developer ###

from pydantic import BaseModel
from service.contact.model.contact import ContactSrv

class ContactApi(BaseModel):
    email: str
    name: str
    content: str

def mapper_model_to_DB(model: ContactApi) -> ContactSrv:
    return ContactSrv(
        email=model.email,
        name=model.name,
        content=model.content
    )
