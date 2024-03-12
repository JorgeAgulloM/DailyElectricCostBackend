from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.subscribers.routes import api_subscribers

app = FastAPI()

app.include_router(api_subscribers.router)

@app.get('/')
def init():
    return {'message': 'Start FastApi'}

@app.get("/ping")
def read_ping():
    return {'response': "pong"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}