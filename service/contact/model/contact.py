### Model Data For Contact to Developer ###

from pydantic import BaseModel
from data.email.models.contact import ContactDB

class ContactSrv(BaseModel):
    email: str
    name: str
    content: str

def mapper_model_to_DB(model: ContactSrv) -> ContactDB:
    return ContactDB(
        email=model.email,
        name=model.name,
        content=model.content
    )
