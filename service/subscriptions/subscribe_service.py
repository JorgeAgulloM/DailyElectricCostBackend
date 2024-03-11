### EMAIL SERVICE ###
from data.db.subscribes.subscribe_repository import search_subscripters, insert_subscription
from service.subscriptions.models.subscripter import SubscriptorSrv, mapper_data_to_service, mapper_service_to_data

def get_subscriptors():
    return search_subscripters()

def insert_subscriptor(subscriptor: SubscriptorSrv):
    return insert_subscription(mapper_service_to_data(subscriptor))
