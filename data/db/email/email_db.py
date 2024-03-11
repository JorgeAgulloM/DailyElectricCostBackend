### EMAIL DB CONNECTION FROM ATLAS_DB/DailyElectricCostDB ###

from typing import Any, Mapping
from pymongo import MongoClient
from data.db.connection.atlas_db_connection import db_client

def _subscripters() -> MongoClient:
    return db_client.subscripters

def db_find():
    return _subscripters.find()

def db_insert_one(field_dict: dict):
    return _subscripters().insert_one(field_dict).insert_one
