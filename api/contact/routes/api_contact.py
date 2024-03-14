### Contact API ###

from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId

from api.contact.model.contact import ContactApi, mapper_model_to_DB
from service.contact.contact_service import contact_developer

router = APIRouter(
    prefix="/contact",
    tags=['contact'], 
    responses = {404: {'message': 'No encontrado'}}
)

#####################################################################################################################
########################################### API CRUD Susbscripters ##################################################
#####################################################################################################################

@router.post('/', status_code=status.HTTP_201_CREATED)
async def contact(contact: ContactApi):
    contact_developer(mapper_model_to_DB(contact))
    return {'message': 'Contact successfully'}
