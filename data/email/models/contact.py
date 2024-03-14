### Model Data For Contact to Developer ###

from pydantic import BaseModel

class ContactDB(BaseModel):
    email: str
    name: str
    content: str
