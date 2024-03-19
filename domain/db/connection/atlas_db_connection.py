### Client Mongo AtlasDB ###
from pymongo import MongoClient
import enviroment_config as env

_url_base: str = env.URL_DB
db_client = MongoClient(_url_base).db
