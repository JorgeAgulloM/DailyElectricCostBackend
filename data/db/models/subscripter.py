### MODEL -> SUBSCRIPTER ###

from typing import Optional
from pydantic import BaseModel

class Subscriptor(BaseModel):
    id: str = Optional[str] | None
    email: str
    activated: bool = False
    date_activated: str = Optional[str] | None
    cancelated: bool = False
    date_cancelated: str = Optional[str] | None
    