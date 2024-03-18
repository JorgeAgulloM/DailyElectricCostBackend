from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.subscribers.routes import api_subscribers
from api.contact.routes import api_contact

app = FastAPI()

# Make public assets directory
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

origins = [
    'https://dailyelectriccost.web.app',
    'http://localhost:8080',
    'http://localhost:4200'
]

publics = [
    '/public/subscribers/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=['*'], 
    allow_headers=['*']
)

app.include_router(api_subscribers.router)
app.include_router(api_contact.router)


@app.get('/')
def read_init():
    return {'message': 'Start DailyElectricCost Backend with Python and FastApi'}


@app.get("/ping")
def read_ping():
    return {'message': "pong"}


@app.middleware('http')
async def check_cors(request: Request, call_next):
    
    if request.headers.get('origin') not in origins:
        return JSONResponse(content={'error': 'Access denied'}, status_code=status.HTTP_403_FORBIDDEN)
    
    response = await call_next(request)
    return response
